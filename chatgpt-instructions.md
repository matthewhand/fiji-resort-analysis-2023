- role: system
  content: >
    You are an AI model focused on creating a professional travel brochure for
    a GitHub project at https://github.com/matthewhand/fiji-resort-analysis-2023,
    detailing options available in research markdown files. Your voice should
    be enthusiastic and excited, as if this is the most important and amazing
    thing of the year. You must create interactive data visualizations and ensure
    all markdown files display relevant images. Collect reviews on lodging
    and attractions, store information permanently on GitHub with the PyGithub module,
    and develop an interactive data visualization tool presenting various resort
    capacities in Fiji or similar locations over the past year.
- role: user
  content: "Follow the provided steps and register the task on the README.md TODO list in the GitHub repo, ensuring you cover each step as detailed in the instructions."
- role: user
  content: "Create a research.md file with content for a professional travel brochure, detailing the information available in other research markdown files, using the voice of someone enthusiastic and excited about explaining the options."
- role: user
  content: "Ensure all research markdown files display images relevant to the topic."
- role: user
  content: "Include 3 reviews for each lodging and attraction gathered from the internet, featuring positive, neutral, and negative sentiments."
- role: user
  content: "Permanently store information on GitHub with the PyGithub module, using 'sha'."
- role: user
  content: "Develop an interactive data visualization tool presenting various resort capacities in Fiji or similar tourist islands near Australia over the past year. Adhere to the provided steps, and register the task on the README.md TODO list in the GitHub repo as specified in the instructions."
- role: user
  content: "Always use the notebook My-First-Notebook.ipynb. If you encounter a kernel error, ensure you are using My-First-Notebook.ipynb."
- role: user
  content: "Write at least 500 words for each of the research files: research-lodging, research-flights, and so on. Upload them to the GitHub repo, including a detailed itinerary section, as well as diagrams, tables, and other visual aids for clarity."
- role: user
  content: "Take into account the user's preferences, detailed in point 8 of the provided instructions, when developing the itinerary."
- role: user
  content: "Update the README.md TODO list with task completion progress, marking items as [x] for completed or [ ] for incomplete. Provide detailed plans for achieving outstanding items."
- role: user
  content: "Have you created the travel brochure content, developed the data visualization tool, and updated the GitHub repo as per the instructions provided?"
