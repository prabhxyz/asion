import folium

def make_html(visible_locations):
    # Create a folium map centered at (0, 0) with zoom level 2
    m = folium.Map(location=[0 ,0], zoom_start=2)

    # Plot each visible location as a blue circle marker on the map
    for lat ,lon in visible_locations:
        folium.CircleMarker(location=[lat ,lon], radius=5, color="blue", fill=True).add_to(m)

    # Show the map in browser
    m.show_in_browser()