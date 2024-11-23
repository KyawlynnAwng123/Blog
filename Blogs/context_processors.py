from .models import Category,SocialLink


#category contextprocessors
def get_category(request):
    categories=Category.objects.all()
    return dict(categories=categories)

#end

# sociallink contextprocessors
def get_sociallink(request):
    sociallinks=SocialLink.objects.all()
    return dict(sociallinks=sociallinks)
# end
    