from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

# Research Task with increased iteration and time limits
research_task = Task(
  description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel video."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
  tools=[yt_tool],
  agent=blog_researcher,
  max_iterations=1000,  # Increase the iteration limit
  time_limit=3600  # Set a 1-hour time limit (in seconds)
)

# Writing Task with increased iteration and time limits
write_task = Task(
  description=(
    "Get the info from the YouTube channel on the topic {topic}."
  ),
  expected_output='Summarize the info from the YouTube channel video on the topic {topic} and create the content for the blog.',
  tools=[yt_tool],
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md',  # Example of output customization
  max_iterations=1000,  # Increase the iteration limit
  time_limit=3600  # Set a 1-hour time limit (in seconds)
)
