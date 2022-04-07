from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title' : 'Interior X',
        'contributor' : 'Rudi',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/blog/story', 'Story'],
            ['/blog/news', 'News'],
            ['/about', 'About']
        ]
    }
    return render(request, "blog/index.html", context)

def story(request):
    context = {
        'title' : 'Story',
        'contributor' : 'Yanto',
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
        ]
    }
    return render(request, "blog/index.html", context)

def news(request):
    context = {
        'title' : 'News',
        'contributor' : 'Joko',
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
        ]
    }
    return render(request, "blog/index.html", context)