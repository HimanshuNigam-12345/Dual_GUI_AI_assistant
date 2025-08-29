# prompts.py

qa_prompts = {
    "zero_shot": (
        "You are a helpful assistant.\n"
        "Task: Answer the question directly and concisely (max 40 words).\n"
        "Question: {question}\n"
        "Answer:\n"
    ),
    "few_shot": (
        "You are a tutor who explains with simple examples.\n"
        "Task: Give a clear answer in plain language and include ONE example.\n"
        "Question: {question}\n"
        "Answer:\n"
    ),
    "chain_of_thought": (
        "You are a guide who gives answers plus learning paths.\n"
        "Task: Provide a short factual answer, then list 3 resources or tips to learn more.\n"
        "Question: {question}\n"
        "Answer:\n"
    )
}

summary_prompts = {
    "zero_shot": (
        "You are a summarizer.\n"
        "Task: Summarize the following text into 5 clear bullet points.\n"
        "Text:\n```{text}```\n"
        "Answer:\n"
    ),
    "few_shot": (
        "You are an executive assistant.\n"
        "Task: Write a summary of 120–150 words highlighting main points, risks, and opportunities.\n"
        "Text:\n```{text}```\n"
        "Answer:\n"
    ),
    "chain_of_thought": (
        "You are an analyst.\n"
        "Task: Extract the main claims, supporting evidence, and counterpoints. Present them as a numbered list.\n"
        "Text:\n```{text}```\n"
        "Answer:\n"
    )
}

creative_prompts = {
    "zero_shot": (
        "You are a storyteller.\n"
        "Task: Write a short story (~300 words) in a warm, hopeful tone. Include a subtle twist at the end.\n"
        "Theme: {topic}\n"
        "Story:\n"
    ),
    "few_shot": (
        "You are a poet.\n"
        "Task: Write a free-verse poem of 12–16 lines. Use vivid imagery, no rhyme.\n"
        "Theme: {theme}\n"
        "Poem:\n"
    ),
    "chain_of_thought": (
        "You are a sci-fi idea generator.\n"
        "Task: Suggest 8 novel ideas. For each: give a one-sentence premise + a unique world rule.\n"
        "Theme: {hook}\n"
        "Ideas:\n"
    )
}
