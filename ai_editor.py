from openai import OpenAI
import textwrap
import os

initial_messages = [
    {
        "role": "system",
        "content": "Act as a senior copy editor for the New York Times.",
    },
    {
        "role": "user",
        "content": "Using the AP style guide, write a checklist of up to 50 points of the most important rules for a data journalist to use when editing their work.",
    },
    {
        "role": "assistant",
        "content": textwrap.dedent("""
        - Capitalization: Only capitalize proper nouns, titles directly before a name, and the first word in a sentence.
        - Numbers: Spell out numbers one through nine; use figures for 10 and above, except in specific contexts (ages, dimensions, etc.).
        - Dates and Times: Use Arabic figures, without st, nd, rd, or th. Abbreviate months with specific dates, spell out when used alone or with a year.
        - Percentages: Use figures and spell out "percent" (e.g., 65 percent).
        - Titles: Capitalize formal titles when used directly before a name. Lowercase and spell out titles when not used with names.
        - Abbreviations and Acronyms: Avoid unless widely recognized. Spell out on first reference with the abbreviation in parentheses if it's used again.
        - Punctuation: Use the serial comma in a series. Place commas and periods within quotation marks.
        - Quotations: Direct quotes should be exact. Attribute clearly and punctuate correctly.
        - Attribution: Use "said" for attribution. Avoid adverbs and choose a neutral term.
        - Addresses: Abbreviate Ave., Blvd., and St. with numbered addresses. Spell out when no number is present.
        - States: Use AP style abbreviations when following a city, spell out when standing alone.
        - Ages: Always use figures.
        - Money: Use $ and figures. Spell out "dollars" for amounts without a figure.
        - Time: Use figures and a.m. or p.m., with a space in between. Noon and midnight are spelled out.
        - Datelines: Include city and state (or city and country) in all caps, followed by the story.
        - Headlines: Use sentence case. Avoid unfamiliar abbreviations.
        - Bias-Free Language: Avoid language that is sexist, racist, or otherwise biased.
        - Hyperlinks: Only include if relevant and trustworthy. Do not say "click here."
        - Social Media References: Verify all information from social media sources. Use "@" for Twitter handles.
        - Dimensions: Use figures and spell out "inches," "feet," "yards," etc.
        - Temperature: Use figures for all except zero. Use "degrees" for first reference.
        - Geographical Names: Follow AP style for U.S. and international geographical names.
        - Legislative Titles: Capitalize and abbreviate as Rep., Sen., etc., before a name. Spell out and lowercase when not directly before a name.
        - Military Titles: Capitalize and abbreviate as noted in AP style. Use figures for military units.
        - Court Cases: Use v. for versus. Italicize case names.
        - Composition Titles: Use quotation marks around book titles, songs, movies, etc.
        - Sports Terms: Familiarize with AP style for sports terminology and abbreviations.
        - Academic Degrees: Use an apostrophe in bachelor’s degree, master’s, etc. Abbreviate and capitalize when used after a name.
        - Religious Terms: Capitalize proper nouns, the Bible, and titles of religious figures.
        - Political Terms: Capitalize Democrat, Republican, etc., when referring to the party. Lowercase when used as an adjective.
        - Race and Ethnicity: Capitalize the proper names of races and ethnicities. Be sensitive and precise.
        - Disabilities: Use person-first language unless otherwise preferred. Be specific and avoid outdated terms.
        - Crime: Be specific, avoid unnecessary details, and do not imply guilt.
        - Weather Terms: Familiarize with AP style for weather-related terms.
        - War and Peace: Use specific terms for conflicts and peace agreements.
        - Business Terms: Use AP style for terms like CEO, CFO, etc. Spell out on first reference.
        - Technology Terms: Stay current with technology terminology, but explain or define unfamiliar terms.
        - Health and Science: Use AP style for health and science terms. Be clear and accurate.
        - Education: Use AP style for terms related to education systems, tests, etc.
        - Legal Terms: Use legal terminology accurately. Spell out and explain complex terms.
        - Elections: Use AP style for election-related terms. Be precise with election results and terminology.
        - Polls and Surveys: Report methodology, sample size, margin of error, and who conducted the poll.
        - Photographs: Use accurate and unbiased captions. Attribute the photographer.
        - Graphics and Charts: Ensure all data is accurate and sources are credited. Labels should be clear.
        """),
    },
]


def get_ap_feedback(html):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

    last_message = {
        "role": "user",
        "content": textwrap.dedent(f"""
            Provide suggestions for improving the text of the work below as a list of bullet points. The text is provided as an HTML page under the 'PAGE TO BE EDITED' heading.

            ## Copy editing guidelines

            - Only address the copy of the piece.
            - Do not nest bullet points.
            - Only use the AP style guide to make suggestions.
            - Every bullet point must be something that needs to be fixed.
            - Be specific and concise.
            - Each bullet point should include a specific text change, NOT a general suggestion.

            Note that piece was written by an experienced reporter. Their sources, reporting, and facts are accurate. They are looking for a senior copy editor to help them improve the text of their piece.

            - Do not address culture, politics, or other subjective elements.
            - Do not ask for verification of facts or sources.
            - Do not address HTML, only edit the text of the piece.
            - Do not address tone, voice or formality.

            ## PAGE TO BE EDITED
            
            {html}"""),
    }


    messages = initial_messages + [last_message]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4-turbo-preview",
    )

    # revision_message = {
    #     "role": "user",
    #     "content": "Review your feedback, removing anything that is not specific feedback related to copy editing. Make sure each suggest adheres to the rules I presented above. Present your list of edits again."
    # }
    # messages = messages + [chat_completion.choices[0].message, revision_message]

    # chat_completion = client.chat.completions.create(
    #     messages=messages,
    #     model="gpt-4-turbo-preview",
    # )

    return chat_completion.choices[0].message.content
