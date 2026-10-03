---
title: Lab instructions
permalink: index.html
layout: home
---
{%- assign course = site.data.course -%}
{%- assign config = site.data.course_config -%}
{%- assign start_url = course.getting_started | replace: '.md', '.html' | prepend: '/' -%}
<link rel="stylesheet" href="{{ '/assets/course/course.css' | relative_url }}?v={{ site.github.build_revision }}">
<div class="course-index" markdown="0">
<h1>Hands-on labs</h1>
<p class="course-intro">{{ config.intro }}</p>
{%- if course.getting_started != "" %}
<div class="course-start">
<div><strong>New to these labs?</strong>{{ config.start_prompt }}</div>
<a class="course-button" href="{{ start_url | relative_url }}">Get started</a>
</div>
{%- endif %}
{%- for section in course.sections %}
{%- assign total_items = 0 -%}{%- assign total_minutes = 0 -%}
{%- for group in section.groups -%}{%- assign total_items = total_items | plus: group.items.size -%}{%- assign total_minutes = total_minutes | plus: group.minutes -%}{%- endfor %}
<p class="course-totals">{{ total_items }} labs &middot; {{ total_minutes }} minutes of hands-on practice{% if config.totals_note %} &middot; {{ config.totals_note }}{% endif %}</p>
{%- for group in section.groups %}
<details class="course-lp" id="{{ group.title | slugify }}" open>
<summary>{{ group.title }}<span class="lp-meta">{{ group.items.size }} labs &middot; {{ group.minutes }} minutes</span></summary>
<div class="lp-body">
{%- if group.learn_url != "" %}
<p class="lp-learn">Related training on Microsoft Learn: <a href="{{ group.learn_url }}">{{ group.learn_title | default: group.title }}</a></p>
{%- endif %}
{%- for item in group.items %}
<div class="lab-card" id="{{ item.label | slugify }}">
<h3><a href="{{ item.url | relative_url }}">{{ item.title }}</a></h3>
{%- if item.minutes %}<span class="course-badge course-badge-time">{{ item.minutes }} minutes</span>{% endif %}{% if item.level %}<span class="course-badge">Level {{ item.level }}</span>{% endif %}{% if item.exercises.size > 0 %}<span class="course-badge">{{ item.exercises.size }} exercises</span>{% endif %}
<p>{{ item.description }}</p>
{%- if item.exercises.size > 0 %}
<ol class="lab-exercises">
{%- for ex in item.exercises %}
<li>{{ ex.title }}{% if ex.minutes %} <span class="ex-min">({{ ex.minutes }} min)</span>{% endif %}</li>
{%- endfor %}
</ol>
{%- endif %}
{%- if item.files.size > 0 %}
<div class="lab-files">Lab files: {% for f in item.files %}<a href="{{ '/' | append: f | relative_url }}" download><code>{{ f | split: '/' | last }}</code></a>{% unless forloop.last %}, {% endunless %}{% endfor %}</div>
{%- endif %}
</div>
{%- endfor %}
</div>
</details>
{%- endfor %}
{%- endfor %}
</div>
<script src="{{ '/assets/course/course.js' | relative_url }}?v={{ site.github.build_revision }}"></script>
