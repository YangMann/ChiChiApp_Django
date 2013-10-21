交大吃吃Web App
================
交大吃吃网页应用 ©2013 交大吃吃，上海交通大学
使用了Django, HTML5, CSS3, Angular.js
大部分网页交互由AJAX完成

# Django模板规范
每个页都从base.html扩展
#### `{% block head %}`扩展`<head>`标签中内容
#### `{% block body %}`扩展`<body>`标签中内容，如果需包含导航菜单，则在第一行`{% include "includes/nav.html" %}`
#### `{% block js-**before/after**-ng %}`扩展`</body>`之前的`<script>`标签，分别位于Angular.js加载前后

# CSS编写规范
## 命名规范
CSS类名以语义化双字母缩写开头（如`nv-`、`fw-`），单词之间使用连字符分割。例如：
    <div class="nv-main-trigger">
        <!-- some tags -->
    </div>
    <!-- some tags -->
    <div class="fw-container">
        <div class="fw-wrapper">
            <!-- some tags -->
        </div>
    </div>

## 响应式框架系统
吃吃仿写了YUI的响应式框架，语法保持一致。例如：
    <div class="g-r">
        <div class="u-1-3"></div>
        <div class="u-2-3"></div>
    </div>
    <div class="g">
        <div class="u-1">
            <div class="g-r">
                <div class="u-1-4"></div>
                <div class="u-3-4"></div>
            </div>
        </div>
    </div>
`class="g"`表示"grid"，显示为一个新框，可以跟上`-r`表示响应式（responsive）。
grid内接`class="u-**分子-分母**"`，表示框内单元格的相对宽度。分式要约分。如果表示整行宽度的单元格，则写为`class="u-1"`。
u内可以嵌套新g。

# JavaScript编写规范
未完待续
