
import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()
        users = response.json()

        if not isinstance(users, list):
            print("Error: Unexpected API response format")
            return None
        
        if num_users > len(users):
            print(
                f"Note: Only {len(users)} users available. Showing all available."
            )
        
        for i in range(min(num_users, len(users))):
            user = users[i]

            name = user.get("name", "Unknown")
            email = user.get("email", "Unknown")
            city = user.get("address", {}).get("city", "Unknown")

            print(f" User {i + 1}:")
            print(f" Name: {name}")
            print(f" Email: {email}")
            print(f" City: {city}")
            print()

            
    except requests.exceptions.ConnectionError:
        print("Error: Network issue - cannot connect to the API")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP error {e.response.status_code} occurred")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Request failed - {e}")
        return None
    except ValueError:
        print("Error: Failed to parse JSON response")
        return None
    
if __name__ == "__main__":
    print("== Fetching first 4 users ===\n")
    fetch_and_display_users(4)

    print("== Fetching first 16 users ===\n")
    fetch_and_display_users(16)