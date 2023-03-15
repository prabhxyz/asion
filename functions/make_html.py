import folium

def make_html(p1, p2, p3, p4):
    m = folium.Map(location=[0, 0], tiles="Stamen Toner", zoom_start=1)
    # Define rectangle coordinates (top-left, bottom-right)
    upper_left = [p4, p1]
    lower_right = [p3, p2]
    rect_coords = [upper_left, lower_right]
    print(rect_coords)
    # Create rectangle overlay
    rect = folium.Rectangle(bounds=rect_coords, fill=True, color='blue', fill_opacity=0.2)
    rect.add_to(m)

    m.show_in_browser()
