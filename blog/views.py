from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'Blog | Kelas Terbuka',
        'heading' : "Blog",
        'subheading' : 'Blog on Kelas Terbuka',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/blog/story', 'Story'],
            ['/blog/news', 'News'],
            ['/about', 'About']
        ],
        "banner": 'blog/img/bannerBlog.png',
    }
    return render(request, "blog/index.html", context)

def story(request):
    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'Story | Kelas Terbuka',
        'heading' : "Story",
        'subheading' : 'Story on Kelas Terbuka',
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
        "banner": 'blog/img/bannerBlog.png',
    }
    return render(request, "blog/index.html", context)

def news(request):
    context = {
        "app_css" : 'blog/css/styles.css',
        'title' : 'News | Kelas Terbuka',
        'heading' : "News",
        'subheading' : "News on Kelas Terbuka",
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
        "banner": 'blog/img/bannerBlog.png',
    }
    return render(request, "blog/index.html", context)