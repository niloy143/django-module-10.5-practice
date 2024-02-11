from django.shortcuts import render
from datetime import datetime
from random import randint

blogs_json = [
    {
        "userId": 1,
        "id": 2,
        "title": "qui est esse",
        "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla",
        "viewers": [
            {"name": "Kuba shamsu", "age": randint(10,40)},
            {"name": "Tarmuj Mia", "age": randint(10,40)},
            {"name": "Karim Molla", "age": randint(10,40)},
            {"name": "Rahim Mola", "age": randint(10,40)},
        ],
        "published": datetime(randint(2020,2023), randint(1,11), randint(1,29)),
        "now": datetime.now(),
    },
    {
        "userId": 1,
        "id": 3,
        "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
        "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut",
        "viewers": [
            {"name": "Kuba shamsu", "age": randint(10,40)},
            {"name": "Tarmuj Mia", "age": randint(10,40)},
            {"name": "Karim Molla", "age": randint(10,40)},
            {"name": "Rahim Mola", "age": randint(10,40)},
        ],
        "published": datetime(randint(2020,2023), randint(1,11), randint(1,29)),
        "now": datetime.now(),
    },
    {
        "userId": 1,
        "id": 4,
        "title": "eum et est occaecati",
        "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit",
        "viewers": [
            {"name": "Kuba shamsu", "age": randint(10,40)},
            {"name": "Tarmuj Mia", "age": randint(10,40)},
            {"name": "Karim Molla", "age": randint(10,40)},
            {"name": "Rahim Mola", "age": randint(10,40)},
        ],
        "published": datetime(randint(2020,2023), randint(1,11), randint(1,29)),
        "now": datetime.now(),
    },
    {
        "userId": 1,
        "id": 5,
        "title": "nesciunt quas odio",
        "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque",
        "viewers": [
            {"name": "Kuba shamsu", "age": randint(10,40)},
            {"name": "Tarmuj Mia", "age": randint(10,40)},
            {"name": "Karim Molla", "age": randint(10,40)},
            {"name": "Rahim Mola", "age": randint(10,40)},
        ],
        "published": datetime(randint(2020,2023), randint(1,11), randint(1,29)),
        "now": datetime.now(),
    },
    {
        "userId": 1,
        "id": 6,
        "title": "dolorem eum magni eos aperiam quia",
        "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae",
        "viewers": [
            {"name": "Kuba shamsu", "age": randint(10,40)},
            {"name": "Tarmuj Mia", "age": randint(10,40)},
            {"name": "Karim Molla", "age": randint(10,40)},
            {"name": "Rahim Mola", "age": randint(10,40)},
        ],
        "published": datetime(randint(2020,2023), randint(1,11), randint(1,29)),
        "now": datetime.now(),
    }
]

def blogs(request):
    return render(request, "blogs.html", {'blogs': blogs_json})

def blog(request, id):
    found_blog = None
    for blog in blogs_json:
        if blog["id"] == id: 
            found_blog = blog
    return render(request, "[blog].html", {'blog': found_blog})