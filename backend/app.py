from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/fetch-feed", methods=["POST"])
def fetch_feed():
    try:
        data = request.get_json()
        auth = data["auth_token"]
        ct0 = data["ct0"]

        headers = {
            "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
            "cookie": f"auth_token={auth}; ct0={ct0}",
            "x-csrf-token": ct0,
            "user-agent": "Mozilla/5.0",
            "referer": "https://x.com/",
        }

        url = "https://x.com/i/api/graphql/Ri47TC1RogqkfaInTxucqA/HomeTimeline"

        variables = {
            "count": 20,
            "includePromotedContent": True,
            "latestControlAvailable": True,
            "requestContext": "launch",
            "withCommunity": True,
        }

        features = {
            "rweb_video_screen_enabled": False,
            "payments_enabled": False,
            "profile_label_improvements_pcf_label_in_post_enabled": True,
            "rweb_tipjar_consumption_enabled": True,
            "verified_phone_label_enabled": True,
            "creator_subscriptions_tweet_preview_api_enabled": True,
            "responsive_web_graphql_timeline_navigation_enabled": True,
            "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
            "premium_content_api_read_enabled": False,
            "communities_web_enable_tweet_community_results_fetch": True,
            "c9s_tweet_anatomy_moderator_badge_enabled": True,
            "responsive_web_grok_analyze_button_fetch_trends_enabled": False,
            "responsive_web_grok_analyze_post_followups_enabled": True,
            "responsive_web_jetfuel_frame": False,
            "responsive_web_grok_share_attachment_enabled": True,
            "articles_preview_enabled": True,
            "responsive_web_edit_tweet_api_enabled": True,
            "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
            "view_counts_everywhere_api_enabled": True,
            "longform_notetweets_consumption_enabled": True,
            "responsive_web_twitter_article_tweet_consumption_enabled": True,
            "tweet_awards_web_tipping_enabled": False,
            "responsive_web_grok_show_grok_translated_post": False,
            "responsive_web_grok_analysis_button_from_backend": True,
            "creator_subscriptions_quote_tweet_preview_enabled": False,
            "freedom_of_speech_not_reach_fetch_enabled": True,
            "standardized_nudges_misinfo": True,
            "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
            "longform_notetweets_rich_text_read_enabled": True,
            "longform_notetweets_inline_media_enabled": True,
            "responsive_web_grok_image_annotation_enabled": True,
            "responsive_web_enhance_cards_enabled": False,
        }

        response = requests.get(
            url,
            headers=headers,
            params={
                "variables": json.dumps(variables),
                "features": json.dumps(features),
            },
        )

        print(f"STATUS: {response.status_code}")

        if response.status_code != 200:
            print("RESPONSE TEXT:", response.text)
            return jsonify({"error": "Failed to fetch feed"}), 400

        json_data = response.json()
        instructions = json_data["data"]["home"]["home_timeline_urt"]["instructions"]

        collected_links = []
        for instr in instructions:
            for entry in instr.get("entries", []):
                tweet_item = (
                    entry.get("content", {})
                    .get("itemContent", {})
                    .get("tweet_results", {})
                    .get("result")
                )
                if tweet_item:
                    tweet_id = tweet_item.get("legacy", {}).get("id_str")
                    username = (
                        tweet_item.get("core", {})
                        .get("user_results", {})
                        .get("result", {})
                        .get("legacy", {})
                        .get("screen_name", "unknown")
                    )
                    if tweet_id and username:
                        tweet_url = f"https://x.com/{username}/status/{tweet_id}"
                        collected_links.append(tweet_url)
                        if len(collected_links) >= 20:
                            break
            if len(collected_links) >= 20:
                break

        print(f"Collected {len(collected_links)} tweets")

        return jsonify(
            {"tweet_count": len(collected_links), "tweet_links": collected_links}
        )

    except Exception as e:
        print("Exception:", str(e))
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    print("Starting Flask server on http://localhost:5000")
    app.run(port=5000)
