import requests

def get_posts(page, per_page):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = response.json()

    # Calculate start and end indices for the posts of the current page
    start = (page - 1) * per_page
    end = start + per_page

    # Return only the posts for the current page
    return posts[start:end]

def main():
    per_page = 5

    while True:
        page = input("Enter the page number (or 'exit' to quit): ")
        if page.lower() == 'exit':
            break

        posts = get_posts(int(page), per_page)

        for i, post in enumerate(posts, 1):
            print(f"Post {i}:")
            print(f"User ID: {post['userId']}")
            print(f"ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}\n")

if __name__ == "__main__":
    main()