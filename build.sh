#! /bin/bash
rm docs/*.html
cat templates/top.html content/home_msg.html      templates/resource_buttons.html      templates/bottom.html > docs/index.html
cat templates/top.html content/skills_msg.html templates/resource_buttons.html content/skills.html templates/bottom.html > docs/abilities.html
cat templates/top.html templates/resource_buttons.html content/projects.html templates/bottom.html > docs/projects.html
