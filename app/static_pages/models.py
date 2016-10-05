from django.core.urlresolvers import reverse

from blog.models import Post


# Blog postuna çok benzediği için birebir kopyaladım, hiçbir override yapmadım.
class StaticPage(Post):

    def get_absolute_url(self):
        view_name = "static_page_detail"
        # view_name = "products:product_detail_slug_function"
        return reverse(view_name, kwargs={"slug": self.slug})