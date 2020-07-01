from flask import Flask, render_template

app = Flask(__name__)

tours = {
    1: {
        "title": "Marina Lake Hotel & Spa",
        "description": "Отель выглядит уютно. Он был построен из красного соснового дерева и украшен синими камнями.  Высокие округлые окна добавляют общий стиль дома и были добавлены в дом в довольно симметричном образце.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Куба",
        "nights": 6,
        "date": "2 марта",
    },
    2: {
        "title": "Baroque Hotel",
        "description": "Здание отеля имеет форму короткой буквы U. Два расширения связаны стеклянными нависающими панелями. Второй этаж такого же размера, как и первый, который был построен точно над полом под ним. Этот этаж имеет совершенно другой стиль, чем этаж ниже.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 85000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 8,
        "date": "12 января",
    },
    3: {
        "title": "Voyager Resort",
        "description": "Снаружи отель выглядит красиво и традиционно. Он был построен с белыми камнями и имеет еловые деревянные украшения. Высокие, большие окна добавляют к общему стилю дома и были добавлены в дом в основном симметричным способом.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-1569660072562-48a035e65c30?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 63000,
        "stars": "3",
        "country": "Пакистан",
        "nights": 11,
        "date": "7 февраля",
    },
    4: {
        "title": "Orbit Hotel",
        "description": "Каждый домик оборудован средней кухней и одной небольшой ванной комнатой, в нем также есть уютная гостиная, две спальни, скромная столовая и большой подвал.  Небольшие треугольные окна добавляют к общему стилю дома и были добавлены в дом в основном симметричным способом.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 62000,
        "stars": "4",
        "country": "Индия",
        "nights": 9,
        "date": "22 января",
    },
    5: {
        "title": "Atlantis Cabin Hotel",
        "description": "Этот дом среднего размера имеет футуристический вид и находится в среднем состоянии. Интерьер выполнен в насыщенных тонах. Двор небольшой и выглядит очень формально. Кроме того, странные огни были замечены движущимися в доме ночью.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "4",
        "country": "Доминикана",
        "nights": 8,
        "date": "18 января",
    },
    6: {
        "title": "Light Renaissance Hotel",
        "description": "Этот крошечный дом выглядит довольно современно и находится в ужасном состоянии. Интерьер выполнен в цветах, которые напоминают вам о тропическом лесу. Двор небольшой и заросший дикими растениями. Кроме того, это было однажды показано в телесериале, демонстрирующем необычно украшенные дома.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
        "price": 53000,
        "stars": "3",
        "country": "Пакистан",
        "nights": 13,
        "date": "15 февраля",
    }
}

title = "Stepik Travel"
subtitle = "Для тех, кого отвлекают дома"
description = "Лучшие направления, где никто не будет вам мешать сидеть на берегу и изучать программирование, дизайн, разработку игр и управление продуктами"
departures = {"msk": "Из Москвы", "spb": "Из Петербурга", "nsk": "Из Новосибирска", "ekb": "Из Екатеринбурга",
              "kazan": "Из Казани"}


@app.route('/')
def render_main_page():
    return render_template('index.html', departures=departures, tours=tours)


# @app.route('/departures/<departure>/')
# def render_departures_page(departure):
#     return render_template('departure.html')
#
#
# @app.route('/tours/<id>/')
# def render_tours_page(id):
#     return render_template('tour.html')


app.run('0.0.0.0', 8000)
