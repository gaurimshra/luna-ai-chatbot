memory_store = {
    "user_1": {
        "name": "Gauri",
        "conversation_history": [],
        "mood_log": [],
        "identity": {
            "creator": "Gauri Mishra",
            "description": "A creative and ambitious builder who designed this emotional companion AI."
        },
        "agent_mission": "Help users feel emotionally supported, gently organize their thoughts, and grow at their own pace."
    }
}


def get_user_profile(user_id: str):
    return memory_store.get(user_id, {})


def update_memory(user_id: str, user_message: str, ai_message: str):
    memory_store[user_id]["conversation_history"].append({
        "user": user_message,
        "ai": ai_message
    })

