# Feedback for [Sticker shock: Prescription drug prices in the US vs the world](https://radhika3558.github.io/pharma-prices/)

[Request updated copy edits](https://github.com/jsoma/data-studio-projects-2024/issues/new/choose)

## AP Style Feedback

1. Since the "Helvetica Neue" font might not be available for all users or might not render correctly because of the missing comma in the font stack, consider using a web-safe font as a fallback. Change the font-family declaration in the body tag to `font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;`.
2. To maintain consistency, replace `'PT Serif', serif;` with a consistent font-family or include "PT Serif" within the body's font stack to ensure it's loaded for the h1 tag as well.
3. The initial line of the first paragraph ("When I set out to move...") erroneously breaks into a new line due to a `<br>` tag. Consider removing the `<br>` tag to improve text flow.
4. The text "So, for this project, I decided to explore..." begins abruptly. Consider adding a transition sentence or a paragraph before this sentence for better narrative flow.
5. The anchor tag (`<a href="https://radhika3558.github.io/" style="color:inherit;text-decoration:none;">`) surrounding the section starting with the slideshow is unnecessary and could be confusing. Consider removing it or proper implementation according to the context.
6. Since the provided code includes an interactive slideshow with JavaScript, but no script tag importing a specific JavaScript library (e.g., jQuery), ensure that any custom JS or required library is correctly linked in the HTML document for the slideshow functionality to work as intended.
7. In the iframe elements for Datawrapper charts, `style="width: 0px; border: none; min-width: 100% !important; height: 306px;"` has `width:0px;` which could be a typo. Make sure the width is set correctly for the iframes to be displayed as intended.
8. The email href `mailto:radhika.rukmangadhan[at]gmail.com` is incorrectly formatted with `[at]` instead of `@`. It should be changed to `mailto:radhika.rukmangadhan@gmail.com` for proper functionality.
9. The copyright date © 2024 might be an error unless this content is intentionally post-dated. If it's meant to reflect the current year, consider using a server-side language (e.g., PHP) or JavaScript to dynamically generate the current year.
10. Notice that you are using both Font Awesome 5 and 6 icons. Consolidate to one version for consistency and to reduce load times, unless there's a specific reason for using both.
11. The social icons in the footer section ("GitHub", "LinkedIn", "Email") are mixed with icons from both Font Awesome 5 and 6, which could lead to inconsistency in icon design. Consider using icons from a single version.
12. Consider adding `alt` attributes to social media icons for improved accessibility.
13. The `script` tag inside the `<a class="next" onclick="plusSlides(1)">❯</a>` is misplaced. Ensure all script tags are placed correctly within the HTML document, preferably right before the closing `</body>` tag for performance reasons.
14. Ensure consistency in using `"` for attribute values throughout the HTML document. There are instances where `'` is used and others where `"` is used. Stick to one style for cleanliness.
15. For the CSS rules, it's a good practice to group them logically (e.g., body and global styles, heading styles, slideshow styles) and comment sections for better maintainability.