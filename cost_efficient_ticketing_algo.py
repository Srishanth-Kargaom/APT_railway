def initialize_station_data():
    """
    Initializes station data with distances.
    """
    stations = [
        (1, "GANDHIDHAM BG - GIMB", 0),
        (2, "BHACHAU BG - BCOB", 38),
        (3, "SAMAKHIALI B G - SIOB", 53),
        (4, "DHRANGDHRA - DHG", 170),
        (5, "VIRAMGAM JN - VG", 235),
        (6, "AHMEDABAD JN - ADI", 300),
        (7, "ANAND JN - ANND", 364),
        (8, "VADODARA JN - BRC", 400),
        (9, "ANKLESHWAR JN- AKV", 479),
        (10, "UDHNA JN - UDN", 533),
        (11, "NANDURBAR - NDB", 689),
        (12, "JALGAON JN - JL", 840),
        (13, "BHUSAVAL JN - BSL", 864),
        (14, "MALKAPUR - MKU", 914),
        (15, "AKOLA JN - AK", 1004),
        (16, "BADNERA JN - BD", 1082),
        (17, "WARDHA JN - WR", 1178),
        (18, "CHANDRAPUR - CD", 1296),
        (19, "BALHARSHAH - BPQ", 1310),
        (20, "SIRPUR KAGAZNGR - SKZR", 1380),
        (21, "RAMAGUNDAM - RDM", 1452),
        (22, "WARANGAL - WL", 1553),
        (23, "KHAMMAM - KMT", 1660),
        (24, "VIJAYAWADA JN - BZA", 1760),
        (25, "ELURU - EE", 1819),
        (26, "RAJAHMUNDRY - RJY", 1909),
        (27, "SAMALKOT JN - SLO", 1959),
        (28, "DUVVADA - DVD", 2092),
        (29, "VISAKHAPATNAM - VSKP", 2110),
    ]
    return stations


def find_possible_routes(stations, boarding, destination):
    """
    Finds all possible combinations of tickets by including prior and later stations.
    Prints the results in ascending order of distance.
    """
    boarding_index = boarding - 1
    destination_index = destination - 1

    # Stations prior to boarding
    prior_stations = stations[:boarding_index + 1]
    # Stations after destination
    later_stations = stations[destination_index:]

    possible_routes = []

    # Generate combinations
    for prior in prior_stations:
        for later in later_stations:
            # Only consider routes where prior is before boarding and later is after destination
            if prior[0] <= boarding and later[0] >= destination:
                total_distance = later[2] - prior[2]
                route = [prior, stations[boarding_index], stations[destination_index], later]
                possible_routes.append((total_distance, route))

    # Sort routes by total distance
    possible_routes.sort(key=lambda x: x[0])

    # Print routes
    print("Possible Routes:")
    for distance, route in possible_routes:
        print(f"Total Distance: {distance} km")
        for station in route:
            print(f"{station[0]}. {station[1]} - {station[2]} km")
        print("-" * 50)


def main():
    stations = initialize_station_data()

    print("Station List:")
    for s_no, name, distance in stations:
        print(f"{s_no}. {name} - {distance} km")

    # Get input for boarding and destination stations
    try:
        boarding = int(input("\nEnter the boarding station number: "))
        destination = int(input("Enter the destination station number: "))

        if boarding < 1 or boarding > len(stations) or destination < 1 or destination > len(stations):
            print("Invalid station numbers! Please enter valid station numbers.")
        else:
            print("\nFinding Possible Routes...\n")
            find_possible_routes(stations, boarding, destination)

    except ValueError:
        print("Invalid input! Please enter valid integers for station numbers.")


if __name__ == "__main__":
    main()