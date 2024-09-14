Завдання 1



Розробіть Python скрипт, який використовує бібліотеку PyMongo для реалізації основних CRUD (Create, Read, Update, Delete) операцій у MongoDB.





Покрокова інструкція



1. Створіть базу даних відповідно до вимог.



Вимоги до структури документа



Кожен документ у вашій базі даних повинен мати наступну структуру:



{
    "_id": ObjectId("60d24b783733b1ae668d4a77"),
    "name": "barsik",
    "age": 3,
    "features": ["ходить в капці", "дає себе гладити", "рудий"]
}



Документ представляє інформацію про кота, його ім'я name, вік age та характеристики features.



2. Розробіть Python скрипт main.py для виконання наступних завдань.





Завдання для виконання:



Читання (Read)

Реалізуйте функцію для виведення всіх записів із колекції.
Реалізуйте функцію, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.


Оновлення (Update)

Створіть функцію, яка дозволяє користувачеві оновити вік кота за ім'ям.
Створіть функцію, яка дозволяє додати нову характеристику до списку features кота за ім'ям.


Видалення (Delete)

Реалізуйте функцію для видалення запису з колекції за ім'ям тварини.
Реалізуйте функцію для видалення всіх записів із колекції.


💡 Рекомендації до виконання:
- Використовуйте MongoDB Atlas або локально встановлений екземпляр MongoDB за допомогою Docker.
- Встановіть бібліотеку PyMongo через pip або інший пакетний менеджер, як pipenv чи poetry.
- Не забудьте обробити можливі винятки при виконанні операцій з базою даних.
- Переконайтеся, що ваші функції чітко коментовані та добре структуровані.
- Заохочується використання Python віртуального середовища для ізоляції залежностей проєкту.


Критерії прийняття



Створено базу даних та виконано вимоги щодо структури документів.
Реалізовано всі необхідні операції.
Оброблено можливі винятки при виконанні операцій з базою даних.
Функції чітко коментовані та добре структуровані.




Завдання 2



Ви повинні виконати скрапінг сайту http://quotes.toscrape.com. Ваша мета отримати два файли: qoutes.json, куди помістіть всю інформацію про цитати, з усіх сторінок сайту та authors.json, де буде знаходитись інформація про авторів зазначених цитат.



Структура файлів json повинна бути наступною:

authors.json



[
  {
    "fullname": "Albert Einstein",
    "born_date": "March 14, 1879",
    "born_location": "in Ulm, Germany",
    "description": "In 1879, Albert Einstein was born in Ulm, Germany. He completed his Ph.D. at the University of Zurich by 1909. His 1905 paper explaining the photoelectric effect, the basis of electronics, earned him the Nobel Prize in 1921. His first paper on Special Relativity Theory, also published in 1905, changed the world. After the rise of the Nazi party, Einstein made Princeton his permanent home, becoming a U.S. citizen in 1940. Einstein, a pacifist during World War I, stayed a firm proponent of social justice and responsibility. He chaired the Emergency Committee of Atomic Scientists, which organized to alert the public to the dangers of atomic warfare.At a symposium, he advised: \\"In their struggle for the ethical good, teachers of religion must have the stature to give up the doctrine of a personal God, that is, give up that source of fear and hope which in the past placed such vast power in the hands of priests. In their labors they will have to avail themselves of those forces which are capable of cultivating the Good, the True, and the Beautiful in humanity itself. This is, to be sure a more difficult but an incomparably more worthy task . . . \\" (\\"Science, Philosophy and Religion, A Symposium,\\" published by the Conference on Science, Philosophy and Religion in their Relation to the Democratic Way of Life, Inc., New York, 1941). In a letter to philosopher Eric Gutkind, dated Jan. 3, 1954, Einstein stated: \\"The word god is for me nothing more than the expression and product of human weaknesses, the Bible a collection of honorable, but still primitive legends which are nevertheless pretty childish. No interpretation no matter how subtle can (for me) change this,\\" (The Guardian, \\"Childish superstition: Einstein's letter makes view of religion relatively clear,\\" by James Randerson, May 13, 2008). D. 1955.While best known for his mass–energy equivalence formula E = mc2 (which has been dubbed \\"the world's most famous equation\\"), he received the 1921 Nobel Prize in Physics \\"for his services to theoretical physics, and especially for his discovery of the law of the photoelectric effect\\". The latter was pivotal in establishing quantum theory.Einstein thought that Newtonion mechanics was no longer enough to reconcile the laws of classical mechanics with the laws of the electromagnetic field. This led to the development of his special theory of relativity. He realized, however, that the principle of relativity could also be extended to gravitational fields, and with his subsequent theory of gravitation in 1916, he published a paper on the general theory of relativity. He continued to deal with problems of statistical mechanics and quantum theory, which led to his explanations of particle theory and the motion of molecules. He also investigated the thermal properties of light which laid the foundation of the photon theory of light.He was visiting the United States when Adolf Hitler came to power in 1933 and did not go back to Germany. On the eve of World War II, he endorsed a letter to President Franklin D. Roosevelt alerting him to the potential development of \\"extremely powerful bombs of a new type\\" and recommending that the U.S. begin similar research. This eventually led to what would become the Manhattan Project. Einstein supported defending the Allied forces, but largely denounced the idea of using the newly discovered nuclear fission as a weapon. Later, with Bertrand Russell, Einstein signed the Russell–Einstein Manifesto, which highlighted the danger of nuclear weapons."
  },
  {
    "fullname": "Steve Martin",
    "born_date": "August 14, 1945",
    "born_location": "in Waco, Texas, The United States",
    "description": "Stephen Glenn \\"Steve\\" Martin is an American actor, comedian, writer, playwright, producer, musician, and composer. He was raised in Southern California in a Baptist family, where his early influences were working at Disneyland and Knott's Berry Farm and working magic and comedy acts at these and other smaller venues in the area. His ascent to fame picked up when he became a writer for the Smothers Brothers Comedy Hour, and later became a frequent guest on the Tonight Show.In the 1970s, Martin performed his offbeat, absurdist comedy routines before packed houses on national tours. In the 1980s, having branched away from stand-up comedy, he became a successful actor, playwright, and juggler, and eventually earned Emmy, Grammy, and American Comedy awards."
  }
]

qoutes.json

[
  {
    "tags": [
      "change",
      "deep-thoughts",
      "thinking",
      "world"
    ],
    "author": "Albert Einstein",
    "quote": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"
  },  
  {
    "tags": [
      "humor",
      "obvious",
      "simile"
    ],
    "author": "Steve Martin",
    "quote": "“A day without sunshine is like, you know, night.”"
  }
]



Створіть хмарну базу даних Atlas MongoDB. Створіть в ній колекції authors та qoutes та імпортуйте дані з відповідних json файлів в MongoDB





Підготовка та завантаження домашнього завдання 



Створіть публічний репозиторій goit-ds-hw-03.
Виконайте завдання та відправте його у свій репозиторій.
Завантажте робочі файли на свій комп’ютер та прикріпіть їх в LMS у форматі zip. Назва архіву повинна бути у форматі ДЗ1_ПІБ.
Прикріпіть посилання на репозиторій goit-ds-hw-023 та відправте на перевірку.


💡 ВАЖЛИВО Перегляньте Інструкцію щодо завантаження робочого файлу з репозиторію на Github




Формат здачі



Прикріплені файли репозиторію у форматі zip з назвою ДЗ1_ПІБ.
Посилання на репозиторій.




Критерії прийняття ДЗ



Прикріплені посилання на репозиторій goit-ds-hw-03 та безпосередньо самі файли репозиторію у форматі zip