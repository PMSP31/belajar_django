from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'Blog | Interior X',
        'heading' : 'Blog on Interior X',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/blog/story', 'Story'],
            ['/blog/news', 'News'],
            ['/about', 'About']
        ],
        "banner": 'blog/img/banner_blog.png',
    }
    return render(request, "index.html", context)

def story(request):
    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'Story | Interior X',
        'heading' : 'Story on Interior X',
        'content' : """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi nulla sint
                    numquam modi, repellat consequuntur a quas labore at nihil, perspiciatis
                    iste vitae odit magnam! Dignissimos assumenda aut reiciendis tempore
                    quaerat error voluptates similique eligendi consectetur molestiae, nihil
                    quis neque rerum consequatur nisi non deserunt animi officiis vel?
                    Dignissimos, dolores!""",
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/blog/story', 'Story'],
            ['/blog/news', 'News'],
            ['/about', 'About']
        ],
        "banner": 'blog/img/banner_blog.png',
    }
    return render(request, "index.html", context)

def news(request):
    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'News | Interior X',
        'heading' : "News on Interior X",
        'content': """Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi nulla sint
                        numquam modi, repellat consequuntur a quas labore at nihil, perspiciatis
                        iste vitae odit magnam! Dignissimos assumenda aut reiciendis tempore
                        quaerat error voluptates similique eligendi consectetur molestiae, nihil
                        quis neque rerum consequatur nisi non deserunt animi officiis vel?

                        Dignissimos, dolores! Lorem ipsum dolor sit amet consectetur adipisicing elit. Quasi nulla sint
                        numquam modi, repellat consequuntur a quas labore at nihil, perspiciatis
                        iste vitae odit magnam! Dignissimos assumenda aut reiciendis tempore
                        quaerat error voluptates similique eligendi consectetur molestiae, nihil
                        quis neque rerum consequatur nisi non deserunt animi officiis vel?
                        Dignissimos, dolores!""",
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/blog/story', 'Story'],
            ['/blog/news', 'News'],
            ['/about', 'About']
        ],
        "banner": 'blog/img/banner_blog.png',
    }
    return render(request, "index.html", context)