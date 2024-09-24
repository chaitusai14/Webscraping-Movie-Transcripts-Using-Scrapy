# Webscraping-Movie-Transcripts-Using-Scrapy

This project is a web crawler built using the **Scrapy** framework, designed to extract movie transcripts from [Subslikescript.com](https://subslikescript.com). The website hosts movie and TV show scripts, and this scraper is capable of navigating through its structure, following links, and automatically collecting movie transcripts.

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Project Structure](#project-structure)
4. [How It Works](#how-it-works)
   - [Crawling Rules](#crawling-rules)
   - [Data Extraction](#data-extraction)
5. [Usage](#usage)
6. [Output](#output)
7. [Customization](#customization)
8. [Future Enhancements](#future-enhancements)

## Overview

This project leverages **web crawling** techniques to automatically discover and extract data from the Subslikescript website. By starting at a given URL and following links within the page, the crawler explores multiple pages and scrapes relevant movie data such as the title, plot summary, and the full transcript. It automates the task of collecting information without manual browsing, making it an efficient tool for extracting large volumes of data.

The web crawler is designed using **Scrapy**, a powerful and efficient Python framework for web scraping and crawling. It not only scrapes individual movie pages but also handles pagination, allowing it to navigate across multiple pages that contain lists of movies.

Key crawling features include:

- **Link extraction**: Automatically identifies and follows links to movie pages from a list of movies.
- **Rule-based crawling**: Uses rules to define what links to follow and what pages to scrape.
- **Pagination handling**: Automatically follows "Next" page links to scrape additional data across multiple pages.
- **Delay between requests**: Prevents overloading the server by introducing a configurable delay between requests.
- **Custom user agent**: Avoids bot detection by simulating a real web browser during the crawling process.

## Features

- **Scrapes Movie Data**: Extracts the movie title, plot summary, and full transcript from each movie page.
- **Pagination Handling**: Automatically follows pagination to scrape multiple pages of movie data.
- **Custom User-Agent**: Uses a custom User-Agent string to mimic a legitimate browser, helping to avoid bot detection.
- **Download Delay**: Configured with a download delay of 0.5 seconds to avoid overloading the target website.

## Requirements

Before running the project, ensure you have the following installed on your system:

- **Python 3.x**: Make sure you have Python 3 installed.
- **Scrapy**: The Scrapy framework is required for this project. You can install it using pip:
  
  ```bash
  pip install scrapy
  ```

## Project Structure

- `Crawling_subslikescript.py`: The main spider code that handles crawling, link extraction, and data parsing.
- `scrapy.cfg`: Configuration file for the Scrapy project.

## How It Works

The crawler specifically targets the section of Subslikescript that lists movies starting with the letter 'X' and scrapes the following information from each movie page:

1. **Movie Title**: The title of the movie.
2. **Plot Summary**: A brief synopsis of the movie plot.
3. **Full Transcript**: The entire script or transcript of the movie.
4. **URL**: The URL of the movie's script page for reference.

### Crawling Rules

- **First Rule**: Extracts movie links from the movie list and calls `parse_item` to extract movie-specific data.
- **Second Rule**: Handles pagination by following the "Next" link to scrape additional pages of movies.

### Data Extraction

On each movie page, the following elements are extracted using XPath selectors:

- Movie title (`h1` tag within the main article).
- Plot summary (the first `p` tag within the main article).
- Full transcript (text from the `div` containing the script).

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/chaitusai14/Webscraping-Movie-Transcripts-Using-Scrapy.git
   cd movie-transcripts-scraper
   ```

2. Install the required dependencies:

   ```bash
   pip install scrapy
   ```

3. To run the spider, use the following command:

   ```bash
   scrapy runspider Crawling_subslikescript.py -o output.json
   ```

   This will start the crawler and save the scraped data to `output.json`.

## Output

The scraper outputs data in JSON format with the following structure for each movie:

```json
{
  "title": "Movie Title",
  "plot": "A brief description of the movie's plot.",
  "transcript": ["Line 1", "Line 2", "Line 3", ...],
  "url": "https://subslikescript.com/movies_letter-X/movie-title"
}
```

## Customization

- **Starting URL**: By default, the scraper targets movies that start with the letter 'X'. You can modify the `start_requests` method in the `Crawling_subslikescript.py` file to start crawling from a different section or letter.

   For example, to scrape movies starting with 'A', change the URL to:

   ```python
   yield scrapy.Request(url='https://subslikescript.com/movies_letter-A',
                        headers={'user-agent': self.user_agent})
   ```

- **Download Delay**: The download delay is set to 0.5 seconds, but you can adjust this in the `custom_settings` to suit your needs.

## Future Enhancements

- **Dynamic Crawling**: Add functionality to crawl movies from all letters or specific genres.
- **Error Handling**: Improve the spider by adding error handling to manage missing data or failed requests.
- **Parallel Scraping**: Enhance the scraper's performance by utilizing Scrapy's built-in concurrency features.

