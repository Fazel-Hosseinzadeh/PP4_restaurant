from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Choices for the status of a post
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
     Stores a single blog post entry related to :model:`auth.User`.

    Attributes:
        title (str): The title of the post, must be unique.
        slug (str): The URL-friendly version of the title, must be unique.
        author (User): The user who authored the post.
        featured_image (CloudinaryField): The image featured in the post, default is 'placeholder'.
        content (str): The main content of the post.
        created_on (datetime): The date and time when the post was created.
        status (int): The status of the post, either 'Draft' (0) or 'Published' (1).
        excerpt (str): A short summary of the post.
        updated_on (datetime): The date and time when the post was last updated.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField("image", default="placeholder")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`Post`.

    Attributes:
        post (ForeignKey): The post that the comment is related to.
        author (ForeignKey): The user who wrote the comment.
        body (TextField): The content of the comment.
        created_on (DateTimeField): The date and time when the comment was
        created.
        approved (BooleanField): Whether the comment is approved for display.
    """

    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments"
                             )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="commenter"
                               )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
