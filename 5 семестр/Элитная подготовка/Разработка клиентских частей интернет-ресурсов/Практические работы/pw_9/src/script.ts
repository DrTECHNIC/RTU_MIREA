// Типы для формы
interface FormData {
    name: string;
    email: string;
    age: string;
    password: string;
    confirmPassword: string;
    role: string;
}

interface ValidationResult {
    isValid: boolean;
    message?: string;
}

type RoleType = 'user' | 'admin' | 'manager' | '';

class RegistrationForm {
    // Элементы формы
    private form!: HTMLFormElement;
    private nameInput!: HTMLInputElement;
    private emailInput!: HTMLInputElement;
    private ageInput!: HTMLInputElement;
    private passwordInput!: HTMLInputElement;
    private confirmPasswordInput!: HTMLInputElement;
    private roleSelect!: HTMLSelectElement;

    // Элементы для отображения ошибок
    private nameError!: HTMLElement;
    private emailError!: HTMLElement;
    private ageError!: HTMLElement;
    private passwordError!: HTMLElement;
    private confirmPasswordError!: HTMLElement;
    private roleError!: HTMLElement;
    private validationSummary!: HTMLElement;
    private successMessage!: HTMLElement;

    // Кнопки
    private resetBtn!: HTMLButtonElement;
    private newRegistrationBtn!: HTMLButtonElement;

    constructor() {
        this.initializeElements();
        this.setupEventListeners();
        this.hideSuccessMessage();
    }

    // Инициализация элементов DOM
    private initializeElements(): void {
        this.form = document.getElementById('registrationForm') as HTMLFormElement;
        this.nameInput = document.getElementById('name') as HTMLInputElement;
        this.emailInput = document.getElementById('email') as HTMLInputElement;
        this.ageInput = document.getElementById('age') as HTMLInputElement;
        this.passwordInput = document.getElementById('password') as HTMLInputElement;
        this.confirmPasswordInput = document.getElementById('confirmPassword') as HTMLInputElement;
        this.roleSelect = document.getElementById('role') as HTMLSelectElement;

        this.nameError = document.getElementById('nameError') as HTMLElement;
        this.emailError = document.getElementById('emailError') as HTMLElement;
        this.ageError = document.getElementById('ageError') as HTMLElement;
        this.passwordError = document.getElementById('passwordError') as HTMLElement;
        this.confirmPasswordError = document.getElementById('confirmPasswordError') as HTMLElement;
        this.roleError = document.getElementById('roleError') as HTMLElement;
        this.validationSummary = document.getElementById('validationSummary') as HTMLElement;
        this.successMessage = document.getElementById('successMessage') as HTMLElement;

        this.resetBtn = document.getElementById('resetBtn') as HTMLButtonElement;
        this.newRegistrationBtn = document.getElementById('newRegistrationBtn') as HTMLButtonElement;
    }

    // Настройка обработчиков событий
    private setupEventListeners(): void {
        this.form.addEventListener('submit', this.handleSubmit.bind(this));
        this.resetBtn.addEventListener('click', this.resetForm.bind(this));
        this.newRegistrationBtn.addEventListener('click', this.showNewRegistration.bind(this));

        // Валидация в реальном времени
        this.nameInput.addEventListener('blur', () => this.validateName());
        this.nameInput.addEventListener('input', () => this.clearError(this.nameInput, this.nameError));

        this.emailInput.addEventListener('blur', () => this.validateEmail());
        this.emailInput.addEventListener('input', () => this.clearError(this.emailInput, this.emailError));

        this.ageInput.addEventListener('blur', () => this.validateAge());
        this.ageInput.addEventListener('input', () => this.clearError(this.ageInput, this.ageError));

        this.passwordInput.addEventListener('blur', () => this.validatePassword());
        this.passwordInput.addEventListener('input', () => {
            this.clearError(this.passwordInput, this.passwordError);
            if (this.confirmPasswordInput.value.length > 0) {
                this.validateConfirmPassword();
            }
        });

        this.confirmPasswordInput.addEventListener('blur', () => this.validateConfirmPassword());
        this.confirmPasswordInput.addEventListener('input', () => this.clearError(this.confirmPasswordInput, this.confirmPasswordError));

        this.roleSelect.addEventListener('change', () => this.validateRole());

        // Добавление кнопки для демо данных
        this.addDemoButton();
    }

    // Скрыть сообщение об успехе
    private hideSuccessMessage(): void {
        this.successMessage.style.display = 'none';
    }

    // Очистка ошибки
    private clearError(input: HTMLInputElement | HTMLSelectElement, errorElement: HTMLElement): void {
        errorElement.textContent = '';
        input.classList.remove('error', 'success');
    }

    // Валидация имени
    private validateName(): ValidationResult {
        const name = this.nameInput.value.trim();
        this.nameError.textContent = '';
        this.nameInput.classList.remove('error', 'success');

        if (name.length === 0) {
            return this.showError(this.nameInput, this.nameError, 'Поле "Имя" обязательно для заполнения');
        }

        if (name.length < 2) {
            return this.showError(this.nameInput, this.nameError, 'Имя должно содержать минимум 2 символа');
        }

        // Проверка, что имя состоит только из букв (и может содержать дефисы и пробелы)
        const nameRegex = /^[A-Za-zА-Яа-яЁё\s\-]+$/;
        if (!nameRegex.test(name)) {
            return this.showError(this.nameInput, this.nameError, 'Имя должно содержать только буквы');
        }

        this.nameInput.classList.add('success');
        return { isValid: true };
    }

    // Валидация email
    private validateEmail(): ValidationResult {
        const email = this.emailInput.value.trim();
        this.emailError.textContent = '';
        this.emailInput.classList.remove('error', 'success');

        if (email.length === 0) {
            return this.showError(this.emailInput, this.emailError, 'Поле "Email" обязательно для заполнения');
        }

        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            return this.showError(this.emailInput, this.emailError, 'Введите корректный email адрес');
        }

        this.emailInput.classList.add('success');
        return { isValid: true };
    }

    // Валидация возраста
    private validateAge(): ValidationResult {
        const age = this.ageInput.value.trim();
        this.ageError.textContent = '';
        this.ageInput.classList.remove('error', 'success');

        if (age.length === 0) {
            return this.showError(this.ageInput, this.ageError, 'Поле "Возраст" обязательно для заполнения');
        }

        const ageNum = parseInt(age, 10);
        if (isNaN(ageNum)) {
            return this.showError(this.ageInput, this.ageError, 'Возраст должен быть числом');
        }

        if (ageNum < 18) {
            return this.showError(this.ageInput, this.ageError, 'Возраст должен быть не менее 18 лет');
        }

        if (ageNum > 120) {
            return this.showError(this.ageInput, this.ageError, 'Введите реальный возраст');
        }

        this.ageInput.classList.add('success');
        return { isValid: true };
    }

    // Валидация пароля
    private validatePassword(): ValidationResult {
        const password = this.passwordInput.value;
        this.passwordError.textContent = '';
        this.passwordInput.classList.remove('error', 'success');

        if (password.length === 0) {
            return this.showError(this.passwordInput, this.passwordError, 'Поле "Пароль" обязательно для заполнения');
        }

        if (password.length < 6) {
            return this.showError(this.passwordInput, this.passwordError, 'Пароль должен содержать минимум 6 символов');
        }

        this.passwordInput.classList.add('success');
        return { isValid: true };
    }

    // Валидация подтверждения пароля
    private validateConfirmPassword(): ValidationResult {
        const password = this.passwordInput.value;
        const confirmPassword = this.confirmPasswordInput.value;
        this.confirmPasswordError.textContent = '';
        this.confirmPasswordInput.classList.remove('error', 'success');

        if (confirmPassword.length === 0) {
            return this.showError(this.confirmPasswordInput, this.confirmPasswordError, 'Подтверждение пароля обязательно');
        }

        if (password !== confirmPassword) {
            return this.showError(this.confirmPasswordInput, this.confirmPasswordError, 'Пароли не совпадают');
        }

        this.confirmPasswordInput.classList.add('success');
        return { isValid: true };
    }

    // Валидация роли
    private validateRole(): ValidationResult {
        const role = this.roleSelect.value as RoleType;
        this.roleError.textContent = '';
        this.roleSelect.classList.remove('error', 'success');

        if (role === '') {
            return this.showError(this.roleSelect, this.roleError, 'Выберите роль');
        }

        const validRoles: RoleType[] = ['user', 'admin', 'manager'];
        if (!validRoles.includes(role)) {
            return this.showError(this.roleSelect, this.roleError, 'Выберите корректную роль');
        }

        this.roleSelect.classList.add('success');
        return { isValid: true };
    }

    // Показать ошибку
    private showError(input: HTMLInputElement | HTMLSelectElement, errorElement: HTMLElement, message: string): ValidationResult {
        errorElement.textContent = message;
        input.classList.add('error');
        return { isValid: false, message };
    }

    // Валидация всей формы
    private validateForm(): boolean {
        const validations = [
            this.validateName(),
            this.validateEmail(),
            this.validateAge(),
            this.validatePassword(),
            this.validateConfirmPassword(),
            this.validateRole()
        ];

        return validations.every(validation => validation.isValid);
    }

    // Получить данные формы
    private getFormData(): FormData {
        return {
            name: this.nameInput.value.trim(),
            email: this.emailInput.value.trim(),
            age: this.ageInput.value.trim(),
            password: this.passwordInput.value,
            confirmPassword: this.confirmPasswordInput.value,
            role: this.roleSelect.value
        };
    }

    // Обработчик отправки формы
    private handleSubmit(event: Event): void {
        event.preventDefault();

        // Скрыть предыдущие сообщения
        this.validationSummary.style.display = 'none';
        this.successMessage.style.display = 'none';

        // Валидируем форму
        if (this.validateForm()) {
            // Форма валидна, показываем сообщение об успехе
            this.form.style.display = 'none';
            this.successMessage.style.display = 'block';

            // Получаем данные формы
            const formData = this.getFormData();

            // Выводим данные формы в консоль (в реальном проекте здесь был бы AJAX запрос)
            console.log('Данные формы:');
            console.log('Имя:', formData.name);
            console.log('Email:', formData.email);
            console.log('Возраст:', formData.age);
            console.log('Роль:', this.roleSelect.options[this.roleSelect.selectedIndex].text);
        } else {
            // Форма невалидна, показываем сводку ошибок
            this.showValidationSummary();
        }
    }

    // Показать сводку ошибок
    private showValidationSummary(): void {
        this.validationSummary.style.display = 'block';
        this.validationSummary.innerHTML = '<h3>Пожалуйста, исправьте следующие ошибки:</h3><ul>';

        // Собираем все ошибки
        const errors: string[] = [];

        if (this.nameError.textContent) errors.push(`<li>${this.nameError.textContent}</li>`);
        if (this.emailError.textContent) errors.push(`<li>${this.emailError.textContent}</li>`);
        if (this.ageError.textContent) errors.push(`<li>${this.ageError.textContent}</li>`);
        if (this.passwordError.textContent) errors.push(`<li>${this.passwordError.textContent}</li>`);
        if (this.confirmPasswordError.textContent) errors.push(`<li>${this.confirmPasswordError.textContent}</li>`);
        if (this.roleError.textContent) errors.push(`<li>${this.roleError.textContent}</li>`);

        this.validationSummary.innerHTML += errors.join('');
        this.validationSummary.innerHTML += '</ul>';
    }

    // Сброс формы
    private resetForm(): void {
        this.form.reset();

        // Очищаем сообщения об ошибках
        this.clearAllErrors();

        // Скрываем сообщения
        this.validationSummary.style.display = 'none';
        this.successMessage.style.display = 'none';

        // Показываем форму, если она была скрыта
        this.form.style.display = 'block';
    }

    // Очистка всех ошибок
    private clearAllErrors(): void {
        const errorElements = [
            { input: this.nameInput, error: this.nameError },
            { input: this.emailInput, error: this.emailError },
            { input: this.ageInput, error: this.ageError },
            { input: this.passwordInput, error: this.passwordError },
            { input: this.confirmPasswordInput, error: this.confirmPasswordError },
            { input: this.roleSelect, error: this.roleError }
        ];

        errorElements.forEach(({ input, error }) => {
            error.textContent = '';
            input.classList.remove('error', 'success');
        });
    }

    // Новая регистрация (кнопка в сообщении об успехе)
    private showNewRegistration(): void {
        this.form.reset();
        this.successMessage.style.display = 'none';
        this.form.style.display = 'block';
        this.clearAllErrors();
    }

    // Добавление кнопки для демо данных
    private addDemoButton(): void {
        const demoButton = document.createElement('button');
        demoButton.type = 'button';
        demoButton.className = 'demo-btn';
        demoButton.innerHTML = '<i class="fas fa-vial"></i> Заполнить тестовыми данными';

        demoButton.addEventListener('click', () => this.fillDemoData());
        demoButton.addEventListener('mouseenter', () => {
            demoButton.style.backgroundColor = '#2980b9';
        });
        demoButton.addEventListener('mouseleave', () => {
            demoButton.style.backgroundColor = '#3498db';
        });

        // Вставляем кнопку перед формой
        const header = document.querySelector('.header');
        if (header) {
            header.insertAdjacentElement('afterend', demoButton);
        }
    }

    // Заполнение формы тестовыми данными
    private fillDemoData(): void {
        this.nameInput.value = 'Алексей';
        this.emailInput.value = 'alexey@example.com';
        this.ageInput.value = '25';
        this.passwordInput.value = 'пароль123';
        this.confirmPasswordInput.value = 'пароль123';
        this.roleSelect.value = 'user';

        // Применяем стили успеха
        this.nameInput.classList.add('success');
        this.emailInput.classList.add('success');
        this.ageInput.classList.add('success');
        this.passwordInput.classList.add('success');
        this.confirmPasswordInput.classList.add('success');
        this.roleSelect.classList.add('success');
    }
}

// Инициализация формы при загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    new RegistrationForm();
});