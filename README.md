# База зананий ПМ-ПУ
### Структура api
`https://pmpulecture.herokuapp.com/api/` - базовый путь к api

* `programmes/` -список всех программ обучения. 
Вывод: 
```JSON
{
  "bachelor": [
    {
      "name": "FIIT",
      "img_url": "https://../KL1QYMBk.jpg"
    },
    {
      "name": "ПМИ",
      "img_url": "https://.../bulevo5.png"
    }
  ],
  "master": [
    {
      "name": "Что-то на маге",
      "img_url": "https://.../ahDf8jg"
    }
  ]
}
```
* `struct/` - вывод предметов на программе

_params_: `programme` - название программы

Вывод:
```JSON
[
  {
    "term": 1,
    "subjects": [
      {
        "id": 2,
        "name": "Матан",
        "lecturers": [
          {
            "id": 3,
            "name": "Платонов"
          },
          {
            "id": 4,
            "name": "Мышков"
          }
        ]
      }
    ]
  },
  {
    "term": 2,
    ...
  }, 
.......,
  {
    "term": 8,
    "subjects": []
  }
]
```

* `lecturer/<int:id>` - вывод информации по лектору по ID

Вывод:
```JSON
{
  "lecturers": {
    "id": 1,
    "name": "Платонов",
    "materials": [
      {
        "Матан": [
          {
            "abstract": [
              {
                "name": "n",
                "url": "http://sfds.com"
              }
            ],
            "questions": [],
            "test": [],
            "other": []
          }
        ]
      },
      .....
    ]
  }
}
```
