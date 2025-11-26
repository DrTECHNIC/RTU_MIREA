class Calculator {
    constructor() {
        this.expressionElement = document.getElementById('expression');
        this.resultElement = document.getElementById('result');
        this.historyList = document.getElementById('history-list');
        this.currentExpression = '';
        this.history = JSON.parse(localStorage.getItem('calculatorHistory')) || [];
        this.shouldResetOnNextInput = false;
        this.isEditing = false;
        this.expressionElement.readOnly = false;
        this.initEventListeners();
        this.loadHistory();
        this.loadLastExpression();
    }

    initEventListeners() {
        const buttons = document.querySelectorAll('.buttons button');
        buttons.forEach(button => {
            button.addEventListener('click', () => {
                const value = button.dataset.value;
                const action = button.dataset.action;
                if (value) this.handleButtonValue(value);
                if (action) this.handleAction(action);
            });
        });
        document.getElementById('clear-history').addEventListener('click', () => {
            this.clearHistory();
        });
        this.expressionElement.addEventListener('keydown', (e) => {
            e.preventDefault();
        });
        this.expressionElement.addEventListener('keypress', (e) => {
            e.preventDefault();
        });
        this.expressionElement.addEventListener('keyup', (e) => {
            e.preventDefault();
        });
        this.expressionElement.addEventListener('paste', (e) => {
            e.preventDefault();
        });
        this.expressionElement.addEventListener('cut', (e) => {
            e.preventDefault();
        });
        this.expressionElement.addEventListener('click', () => {
            this.isEditing = true;
            this.shouldResetOnNextInput = false;
        });
        this.expressionElement.addEventListener('focus', () => {
            this.isEditing = true;
            this.shouldResetOnNextInput = false;
        });
        this.expressionElement.addEventListener('blur', () => {
            this.isEditing = false;
        });
        this.expressionElement.addEventListener('contextmenu', (e) => {
            e.preventDefault();
        });
    }

    handleButtonValue(value) {
        if (this.shouldResetOnNextInput && !this.isEditing) {
            this.clear();
            this.shouldResetOnNextInput = false;
        }
        const cursorPosition = this.expressionElement.selectionStart;
        const selectionEnd = this.expressionElement.selectionEnd;
        if (cursorPosition !== selectionEnd) {
            this.currentExpression =
                this.currentExpression.substring(0, cursorPosition) +
                value +
                this.currentExpression.substring(selectionEnd);
        }
        else {
            if (value === '.') {
                const currentNumber = this.getCurrentNumberAtCursor(cursorPosition);
                if (currentNumber && currentNumber.includes('.'))
                    return;
            }
            this.currentExpression =
                this.currentExpression.substring(0, cursorPosition) +
                value +
                this.currentExpression.substring(cursorPosition);
        }
        this.updateDisplay();
        const moveBy = value === '**' ? 2 : 1;
        const newCursorPosition = cursorPosition + moveBy;
        setTimeout(() => {
            this.expressionElement.setSelectionRange(newCursorPosition, newCursorPosition);
        }, 0);
        this.isEditing = true;
    }

    getCurrentNumberAtCursor(cursorPosition) {
        const beforeCursor = this.currentExpression.substring(0, cursorPosition);
        const afterCursor = this.currentExpression.substring(cursorPosition);
        let start = beforeCursor.length - 1;
        while (start >= 0 && /[\d\.]/.test(beforeCursor[start]))
            start--;
        start++;
        let end = 0;
        while (end < afterCursor.length && /[\d\.]/.test(afterCursor[end]))
            end++;
        return beforeCursor.substring(start) + afterCursor.substring(0, end);
    }

    handleAction(action) {
        switch(action) {
            case 'clear':
                this.clear();
                break;
            case 'backspace':
                this.backspace();
                break;
            case 'calculate':
                this.calculate();
                break;
            case 'add':
                this.handleButtonValue('+');
                break;
            case 'subtract':
                this.handleButtonValue('-');
                break;
            case 'multiply':
                this.handleButtonValue('*');
                break;
            case 'divide':
                this.handleButtonValue('/');
                break;
            case 'percent':
                this.handleButtonValue('%');
                break;
            case 'power':
                this.handleButtonValue('**');
                break;
        }
    }

    clear() {
        this.currentExpression = '';
        this.resultElement.textContent = '';
        this.updateDisplay();
        this.shouldResetOnNextInput = false;
        this.isEditing = false;
    }

    backspace() {
        const cursorPosition = this.expressionElement.selectionStart;
        const selectionEnd = this.expressionElement.selectionEnd;
        if (cursorPosition !== selectionEnd) {
            this.currentExpression =
                this.currentExpression.substring(0, cursorPosition) +
                this.currentExpression.substring(selectionEnd);
            this.updateDisplay();
            setTimeout(() => {
                this.expressionElement.setSelectionRange(cursorPosition, cursorPosition);
            }, 0);
        }
        else if (cursorPosition > 0) {
            this.currentExpression =
                this.currentExpression.substring(0, cursorPosition - 1) +
                this.currentExpression.substring(cursorPosition);
            this.updateDisplay();
            setTimeout(() => {
                this.expressionElement.setSelectionRange(cursorPosition - 1, cursorPosition - 1);
            }, 0);
        }
        this.shouldResetOnNextInput = false;
        this.isEditing = true;
    }

    calculate() {
        if (!this.currentExpression)
            return;
        try {
            let expression = this.currentExpression;
            expression = expression.replace(/×/g, '*').replace(/÷/g, '/');
            const result = eval(expression);
            const formattedResult = this.formatResult(result);
            this.saveToHistory(this.currentExpression, formattedResult);
            this.resultElement.textContent = formattedResult;
            this.saveLastExpression();
            this.shouldResetOnNextInput = true;
            this.isEditing = false;
        } catch (error) {
            this.resultElement.textContent = 'Ошибка';
            this.shouldResetOnNextInput = true;
        }
    }

    formatResult(result) {
        if (typeof result === 'number') {
            if (Math.abs(result) < 1e-10)
                result = 0;
            if (Math.abs(result) > 1e12)
                return result.toExponential(6);
            if (!Number.isInteger(result))
                return parseFloat(result.toFixed(10)).toString();
        }
        return result.toString();
    }

    saveToHistory(expression, result) {
        const historyItem = {
            expression,
            result,
            timestamp: new Date().toLocaleString()
        };
        this.history.unshift(historyItem);
        if (this.history.length > 10)
            this.history.pop();
        this.saveHistory();
        this.loadHistory();
    }

    loadHistory() {
        this.historyList.innerHTML = '';
        this.history.forEach(item => {
            const historyElement = document.createElement('div');
            historyElement.className = 'history-item';
            historyElement.innerHTML = `
                <div class="history-expression">${item.expression}</div>
                <div class="history-result">= ${item.result}</div>
            `;
            historyElement.addEventListener('click', () => {
                this.currentExpression = item.expression;
                this.resultElement.textContent = item.result;
                this.updateDisplay();
                this.shouldResetOnNextInput = true;
                this.isEditing = false;
                setTimeout(() => {
                    this.expressionElement.setSelectionRange(
                        this.currentExpression.length,
                        this.currentExpression.length
                    );
                }, 0);
            });
            this.historyList.appendChild(historyElement);
        });
    }

    clearHistory() {
        this.history = [];
        this.saveHistory();
        this.loadHistory();
    }

    saveHistory() {
        localStorage.setItem('calculatorHistory', JSON.stringify(this.history));
    }

    saveLastExpression() {
        localStorage.setItem('lastExpression', this.currentExpression);
        localStorage.setItem('lastResult', this.resultElement.textContent);
    }

    loadLastExpression() {
        const lastExpression = localStorage.getItem('lastExpression');
        const lastResult = localStorage.getItem('lastResult');
        if (lastExpression) {
            this.currentExpression = lastExpression;
            this.resultElement.textContent = lastResult || '';
            this.updateDisplay();
        }
    }

    updateDisplay() {
        this.expressionElement.value = this.currentExpression;
        this.expressionElement.scrollLeft = this.expressionElement.scrollWidth;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new Calculator();
});
