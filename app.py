from flask import Flask, jsonify, request
import requests
from user_agent import generate_user_agent
app = Flask(__name__)

# Define a function that applies a character mapping to a string
def apply_namemap(input_string, namemap):
    result = ''  # Initialize an empty string to store the transformed string
    for char in input_string:  # Iterate through each character in the input string
        if char in namemap:  # Check if the character exists in the namemap
            result += namemap[char]  # If it does, replace it with the corresponding value from the namemap
        else:
            result += char  # If not, keep the original character
    return result  # Return the transformed string

# Example usage of the apply_namemap function:
namemap = {  # Define a character mapping dictionary
    'c': '3',
    'f': '0',
    '2': 'd',
    '1': 'e',
    '8': '7',
    '9': '6',
    'a': '5',
    'b': '4',
    '3': 'c',
    '0': 'f',
    'd': '2',
    'e': '1',
    '7': '8',
    '6': '9',
    '5': 'a',
    '4': 'b',
}

@app.route('/<code>')
def hello_world(code):
    # Check if "fh_" is present in the code parameter
    if "fh_" in code:
        # If found, remove "fh_" from the code
        code = code.replace("fh_", "")

    # Apply the namemap to the modified code
    output_string = apply_namemap(code, namemap)

    response = {
        "password": f'wlan{output_string}'
    }
    return jsonify(response)

@app.route('/tiktok/<user>')
def tiktok(user):
    url = f'https://tiktok-video-no-watermark2.p.rapidapi.com/user/info?unique_id={user}&user_id='
    headers = {
        'X-RapidAPI-Host': 'tiktok-video-no-watermark2.p.rapidapi.com',
        'X-RapidAPI-Key': '54eb4910e1msh0b7d1211a1be475p12c3aejsnd55f85d359f3',
        'Host': 'tiktok-video-no-watermark2.p.rapidapi.com',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.14.7',
    }
    response = requests.get(url, headers=headers)  # Use requests module to make HTTP request
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: {response.status_code}"
@app.route("/insta/<username>")
def get_instagram_info(username):
    try:
        gd = str(generate_user_agent())

        url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'viewport-width': '412',
            'x-asbd-id': '198387',
            'x-ig-app-id': '1217981644879628',
            'user-agent': gd
        }

        r4 = requests.get(url, headers=headers).json()

        data = r4['data']['user']
        id = data['id']

        private = "Public" if data['is_private'] == "False" else "Private"
        posts = data['edge_owner_to_timeline_media']['count']
        full_name = data['full_name']
        username = data['username']
        followers = data['edge_followed_by']['count']
        following = data['edge_follow']['count']
        bio = data['biography']
        info = {
            'username': username,
            'full_name': full_name,
            'id': id,
            'private': private,
            'followers': followers,
            'following': following,
            'posts': posts,
            'bio': bio,
            'Telegram': '@y9hba, @zitdo'
        }
        return jsonify(info)
    except Exception as e:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run()

