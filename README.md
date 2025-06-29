# Headlines-Scrap-
| Step | Action                       | Purpose                              |
| ---- | ---------------------------- | ------------------------------------ |
| 1    | Import libraries             | Use tools for web requests & parsing |
| 2    | Set URL and headers          | Target BBC and mimic browser         |
| 3    | Send request                 | Get HTML content                     |
| 4    | Check status code            | Ensure page loaded                   |
| 5    | Parse with BeautifulSoup     | Navigate HTML structure              |
| 6    | Find all `<h3>` tags         | Locate headlines                     |
| 7    | Clean and store text         | Avoid duplicates or blank entries    |
| 8    | Write to `bbc_headlines.txt` | Save for later use                   |
| 9    | Print success message        | Confirm completion                   |
| 10   | Handle exceptions            | Avoid crash on error                 |
