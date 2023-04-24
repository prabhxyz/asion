import os
import folium
import webbrowser

def make_html(visible_locations):
    # Create a folium map centered at (0, 0) with zoom level 2
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Plot each visible location as a blue circle marker on the map
    for lat, lon in visible_locations:
        folium.CircleMarker(location=[lat, lon], radius=5, color="blue", fill=True, auto_open=False).add_to(m)

    # Show the map in browser
    html_path = "data/visible_locations.html"

    m.save(html_path)
    webbrowser.open('file://' + os.path.realpath(html_path))