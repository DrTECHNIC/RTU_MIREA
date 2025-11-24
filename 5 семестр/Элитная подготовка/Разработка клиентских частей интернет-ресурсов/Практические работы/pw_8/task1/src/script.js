// 1. Создаем массив JSON с данными для карточек
const cardsData = [
    {
        id: 1,
        title: "Искусственный интеллект в современном мире",
        text: "Искусственный интеллект трансформирует различные отрасли, от медицины до финансов. Узнайте, как ИИ меняет нашу повседневную жизнь.",
        image: "https://12-kanal.ru/upload/iblock/62a/zb1mq2841smduhwwuv3jwjfv9eooyc50/fotograf3.jpg",
        author: {
            name: "Алексей Петров",
            role: "Эксперт по ИИ",
            avatar: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1HLt964JQLk0k-6rKs389WMjtwgYNyWggsg&s",
            icon: "https://cdn-icons-png.flaticon.com/512/25/25231.png"
        }
    },
    {
        id: 2,
        title: "Устойчивое развитие и экологичный образ жизни",
        text: "Как каждый из нас может внести вклад в сохранение планеты через простые ежедневные привычки и осознанное потребление.",
        image: "https://12-kanal.ru/upload/iblock/62a/zb1mq2841smduhwwuv3jwjfv9eooyc50/fotograf3.jpg",
        author: {
            name: "Мария Иванова",
            role: "Эколог",
            avatar: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1HLt964JQLk0k-6rKs389WMjtwgYNyWggsg&s",
            icon: "https://cdn-icons-png.flaticon.com/512/25/25231.png"
        }
    },
    {
        id: 3,
        title: "Цифровая трансформация бизнеса",
        text: "Как современные технологии помогают компаниям адаптироваться к быстро меняющимся условиям рынка и повышать эффективность.",
        image: "https://12-kanal.ru/upload/iblock/62a/zb1mq2841smduhwwuv3jwjfv9eooyc50/fotograf3.jpg",
        author: {
            name: "Дмитрий Смирнов",
            role: "Бизнес-консультант",
            avatar: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1HLt964JQLk0k-6rKs389WMjtwgYNyWggsg&s",
            icon: "https://cdn-icons-png.flaticon.com/512/25/25231.png"
        }
    },
    {
        id: 4,
        title: "Психология продуктивности",
        text: "Научно обоснованные методы повышения личной эффективности и управления временем в условиях многозадачности.",
        image: "https://12-kanal.ru/upload/iblock/62a/zb1mq2841smduhwwuv3jwjfv9eooyc50/fotograf3.jpg",
        author: {
            name: "Ольга Козлова",
            role: "Психолог",
            avatar: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1HLt964JQLk0k-6rKs389WMjtwgYNyWggsg&s",
            icon: "https://cdn-icons-png.flaticon.com/512/25/25231.png"
        }
    },
    {
        id: 5,
        title: "Будущее удаленной работы",
        text: "Как пандемия изменила подход к организации труда и какие тенденции сохранятся в постковидную эпоху.",
        image: "https://12-kanal.ru/upload/iblock/62a/zb1mq2841smduhwwuv3jwjfv9eooyc50/fotograf3.jpg",
        author: {
            name: "Сергей Васильев",
            role: "HR-эксперт",
            avatar: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1HLt964JQLk0k-6rKs389WMjtwgYNyWggsg&s",
            icon: "https://cdn-icons-png.flaticon.com/512/25/25231.png"
        }
    },
    {
        id: 6,
        title: "Инновации в образовании",
        text: "Технологии виртуальной реальности, геймификация и персонализированное обучение - как меняется современное образование.",
        image: "https://12-kanal.ru/upload/iblock/62a/zb1mq2841smduhwwuv3jwjfv9eooyc50/fotograf3.jpg",
        author: {
            name: "Екатерина Новикова",
            role: "Педагог-новатор",
            avatar: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1HLt964JQLk0k-6rKs389WMjtwgYNyWggsg&s",
            icon: "https://cdn-icons-png.flaticon.com/512/25/25231.png"
        }
    }
];

// 2. Функция для создания одной карточки
function createCard(cardData) {
    // Создаем основной элемент карточки
    const card = document.createElement('div');
    card.className = 'card';

    // Создаем изображение карточки
    const image = document.createElement('img');
    image.className = 'main-image';
    image.src = cardData.image;
    image.alt = cardData.title;

    // Создаем контейнер для текстового содержимого
    const contentWrapper = document.createElement('div');
    contentWrapper.className = 'content-wrapper';

    // Создаем текстовый блок
    const textBlock = document.createElement('div');
    textBlock.className = 'Text';

    const title = document.createElement('h3');
    title.textContent = cardData.title;

    const text = document.createElement('p');
    text.textContent = cardData.text;

    textBlock.appendChild(title);
    textBlock.appendChild(text);

    // Создаем блок автора
    const authorBlock = document.createElement('div');
    authorBlock.className = 'Author';

    const avatar = document.createElement('img');
    avatar.className = 'avatar';
    avatar.src = cardData.author.avatar;
    avatar.alt = cardData.author.name;

    const authorInfo = document.createElement('div');
    authorInfo.className = 'author-info';

    const authorName = document.createElement('h4');
    authorName.textContent = cardData.author.name;

    const authorRole = document.createElement('p');
    authorRole.textContent = cardData.author.role;

    authorInfo.appendChild(authorName);
    authorInfo.appendChild(authorRole);

    const icon = document.createElement('img');
    icon.className = 'icon';
    icon.src = cardData.author.icon;
    icon.alt = 'Иконка';

    authorBlock.appendChild(avatar);
    authorBlock.appendChild(authorInfo);
    authorBlock.appendChild(icon);

    // Собираем карточку
    contentWrapper.appendChild(textBlock);
    contentWrapper.appendChild(authorBlock);

    card.appendChild(image);
    card.appendChild(contentWrapper);

    return card;
}

// 3. Функция для создания всех карточек и добавления их в контейнер
function renderCards() {
    const container = document.getElementById('cards-container');

    // Очищаем контейнер перед добавлением новых карточек
    container.innerHTML = '';

    // Создаем и добавляем карточки в контейнер
    cardsData.forEach(cardData => {
        const cardElement = createCard(cardData);
        container.appendChild(cardElement);
    });
}

// Вызываем функцию отрисовки карточек после загрузки DOM
document.addEventListener('DOMContentLoaded', renderCards);