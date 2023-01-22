import folium
from django.shortcuts import render
from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon
from folium import LayerControl
from folium import plugins

def city_map(request):
    template = 'map_nn/showmap.html'

    m = folium.Map(width="100%", height="100%", location=[56.326844, 44.006543], zoom_start = 12, control_scale=True)
    folium.Marker(location=[56.326844, 44.006543], popup = "Нижний Новгород", icon=folium.Icon(color = 'red')).add_to(m)
    formatter = "function(num) {return L.Util.formatNum(num, 5);};"

    mouse_position = MousePosition(
        position='topright',
        separator=' Long: ',
        empty_string='NaN',
        lng_first=False,
        num_digits=20,
        prefix='Lat:',
        lat_formatter=formatter,
        lng_formatter=formatter,
    )

    m.add_child(mouse_position)

    lat = [
        56.328614,
        56.325129,
        56.323554,
        56.320048,
        56.319195,
    ]
    lon = [
        44.003085,
        44.019444,
        44.047114,
        43.998834,
        43.964878,
    ]
    descriptions = [
        'Нижегородский Кремль. Наиболее посещаемая достопримечательность города.Сооружение начала XVI в. Наиболее значительная постройка на территории кремля - Михайло-Архангельский собор (XVII в.)',
        'Усадьба В.М. Рукавишникова',
        'Западные ворота',
        'Нижегородское отделение Государственного банка',
        'Нижегородский метромост. Совмещённый мостовой переход через Оку в Нижнем Новгороде. Соединяет верхнюю часть города с нижней.',
    ]

    Attraction = folium.FeatureGroup(name='Достопримечательности').add_to(m)
    
    for lat, lon, descriptions in zip(lat, lon, descriptions):
        folium.Marker(location=[lat, lon], popup=str(descriptions), icon=folium.Icon(color = 'gray')).add_to(Attraction)

    folium.raster_layers.TileLayer('Open Street Map').add_to(m)
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)

    # add full screen button to map
    plugins.Fullscreen().add_to(m)
    draw = plugins.Draw(export=True)
    # add draw tools to map
    draw.add_to(m)


    layer_control = LayerControl()
    m.add_child(layer_control)

    return render(request, template, {'map': m._repr_html_()}, )
