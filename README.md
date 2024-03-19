# LAB-ORM-1

## Using what you learned , Create a  new project `BlogWebsite`:
- Users can view the blog posts in the home page.
- Users can Add a new blog post. 


### Create model `Post` , it should have the following attributes :
- title : char field 
- content : text field
- is_published : boolean field
- published_at : datetime field

## Using your LAB-ORM-1 , do the following:
- Add detail page.✅
- Add update page.✅
- Add ability to delete.✅
- Deal with not_found pages (display a page if a user tries to display detail for a post that doesn't exist)✅
- Add poster filed to your Post model.✅
- in the Add post & update Post , let the user choose a poster.✅
- Add a category field to your post model (use TextChoices) choices are : General, Science, Culture, Food, Tech, Fashion ✅

After you finish , sync your changes to githbu & create a Pull Request.

## Using your last LAB , do the following:
 
- Limit posts in the home page to 3 pages, and display only published posts. ✅
- Add a new page to display all the posts.✅
- In the new page , add filter by category (display the chosen category, with the result count) ✅
- Add a search page : user can search for a post, user can filter by publish date .
Hint: use a form with method = “get” attribute to help you build Query.

After you finish , sync your changes to githbu & create a Pull Request 