var myMap;

    ymaps.ready(init);

    function init() {
        myMap = new ymaps.Map('map', {
            center: [56.85, 60.6], // Екб
            zoom: 10
        });

        // Обработка отправки формы
        document.getElementById('locationForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Отменяем стандартное поведение отправки формы

            var club = document.getElementById('clubSelect').value;
            var address = club;

            // Выполняем геокодирование для адреса клуба
            ymaps.geocode(address).then(function (res) {
                var firstGeoObject = res.geoObjects.get(0);
                var coordinates = firstGeoObject.geometry.getCoordinates();

                // Удаляем предыдущие метки с карты
                myMap.geoObjects.removeAll();

                // Добавляем метку на карту
                var myPlacemark = new ymaps.Placemark(coordinates, {
                    hintContent: 'Место',
                    balloonContent: 'Описание места'
                });

                myMap.geoObjects.add(myPlacemark);

                // Центрируем карту по координатам метки
                myMap.setCenter(coordinates);
            });
        });
    }