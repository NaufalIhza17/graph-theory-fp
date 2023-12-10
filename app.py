from api import GOOGLE_API_KEY
from calculate_shortest_route import calculate_shortest_route

def main():
    api_key = GOOGLE_API_KEY 

    current_location = input("Enter your current location (city): ").strip()
    mode = input("Enter the mode of travel (walking, biking, driving): ").strip().lower()

    num_destinations = int(input("Enter the number of destinations (more than 2): "))
    destinations = [input(f"Enter destination #{i + 1}: ").strip() for i in range(num_destinations)]

    shortest_route = calculate_shortest_route(api_key, [current_location], destinations, mode)

    if shortest_route:
        sorted_destinations = sorted(shortest_route.items(), key=lambda x: x[1]['distance'])
        
        print("\nSorted Places based on Distance:")
        for node, data in sorted_destinations:
            print(f"To {node}: Distance: {data['distance']} meters, Time: {data['time']} seconds")

if __name__ == "__main__":
    main()
