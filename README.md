# GraphQL (Graph Query Language) for APIs

http://www.graphql.org

<p style='text-align: justify;'>
GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, makes it easier to evolve APIs over time, and enables powerful developer tools.
</p>

---

### Build a simple blog API service. It should expose a GraphQL endpoint to do the following things:

1. Implement a `createPost()` mutation which will create a `Post` (a blogpost object) with attributes {`title`, `description`, `publish_date`, `author` (just a name as TextField)}
2. Implement a `updatePost($id)` mutation which will update a `Post` attributes by `$id`
3. Implement a `createComment()` mutation which will create a `Comment` object with attributes {`post` (the blogpost object), `text`, `author` (just the name as a TextField)}
4. Implement a `deleteComment($id)` mutation to delete the given `Comment` by its ID.
5. Implement a `posts()` query to list all the posts
6. Implement a `post($id)` query to get details of a post and all its comments

---

### Technology used:

1. GraphQL
2. Python
   - Django framework
   - Graphene package
3. SQLite database

---

### Project setup:

1. Clone the git repository from the link\
   https://github.com/SandeepR1305/GRAPHQL

2. Activate the Python virtual environment
   > `cd GRAPHQL/env/Scripts/activate`
3. install the Python packages

   > `pip install django`\
   > `pip install graphene-django`

4. Run Django Server.

   > `python manage.py runserver`\
   > Click on this link : http://127.0.0.1:8000/graphql

---

### Examples:

#### 1. createPost()

```python
# input
mutation MyMutation {
createPost(
 author: "Sandeep"
 description: "this GraphQL post"
 title: "GraphQL post"
) {
 post {
   id
   title
   author
   description
   publishDate
 }
}
}
```

```json
# output
{
  "data": {
    "createPost": {
      "post": {
        "id": "7",
        "title": "GraphQL post",
        "author": "Sandeep",
        "description": "this GraphQL post",
        "publishDate": "2023-10-11"
      }
    }
  }
}
```

#### 2. updatePost()

```python
# input
mutation MyMutation {
  updatePost(
    id: 7
    title: "GraphQL post"
    author: "Sandeep Mundergi"
    description: "this GraphQL post"
  ) {
    post{
      id
      author
      title
      description
      publishDate
    }
  }
}
```

```json
# output
{
  "data": {
    "updatePost": {
      "post": {
        "id": "7",
        "author": "Sandeep Mundergi",
        "title": "GraphQL post",
        "description": "this GraphQL post",
        "publishDate": "2023-10-11"
      }
    }
  }
}
```

#### 3. createComment()

```python
# input
mutation MyMutation {
  createComment(
    author: "sandy"
    postId: "7"
    text: "this is comment for  GraphQL"
  ) {
    comment {
      id
      author
      text
    }
  }
}
```

```json
# output
{
  "data": {
    "createComment": {
      "comment": {
        "id": "4",
        "author": "sandy",
        "text": "this is comment for  GraphQL"
      }
    }
  }
}
```

#### 4. deleteComment()

```python
# input
mutation MyMutation {
  deleteComment(id: "4") {
    success
  }
}
```

```json
# output
{
  "data": {
    "deleteComment": {
      "success": true
    }
  }
}
```

#### 5. post()

```python
# input
query MyQuery {
  post(id: "7") {
    id
    author
    title
    publishDate
    description
  }
}
```

```json
# output
{
  "data": {
    "post": {
      "id": "7",
      "author": "Sandeep Mundergi",
      "title": "GraphQL post",
      "publishDate": "2023-10-11",
      "description": "this GraphQL post"
    }
  }
}
```

#### 6. posts()

```python
# input
query MyQuery {
  posts{
    id
    author
    title
    publishDate
    description
  }
}
```

```json
# output
{
  "data": {
    "posts": [
      {
        "id": "5",
        "author": "sandeep",
        "title": "new post",
        "publishDate": "2023-10-11",
        "description": "this is new post created by sandeep"
      },
      {
        "id": "6",
        "author": "Sandeep",
        "title": "New Post",
        "publishDate": "2023-10-11",
        "description": "this is new post created by sandeep"
      },
      {
        "id": "7",
        "author": "Sandeep Mundergi",
        "title": "GraphQL post",
        "publishDate": "2023-10-11",
        "description": "this GraphQL post"
      }
    ]
  }
}
```

#### 7. comment()

```python
# input
query MyQuery {
  comment(id:5) {
    id
    author
    text
    post {
      id
      author
      title
    }
  }
}
```

```json
# output
{
  "data": {
    "comment": {
      "id": "5",
      "author": "Bean",
      "text": "this is comment",
      "post": {
        "id": "7",
        "author": "Sandeep Mundergi",
        "title": "GraphQL post"
      }
    }
  }
}
```

#### 8. comments()

```python
# input
query MyQuery {
  comments {
    id
    author
    text
    post {
      id
      author
      title
    }
  }
}
```

```json
# output
{
  "data": {
    "comments": [
      {
        "id": "5",
        "author": "Bean",
        "text": "this is comment",
        "post": {
          "id": "7",
          "author": "Sandeep Mundergi",
          "title": "GraphQL post"
        }
      },
      {
        "id": "4",
        "author": "JOY",
        "text": "this is comment 2",
        "post": {
          "id": "7",
          "author": "Sandeep Mundergi",
          "title": "GraphQL post"
        }
      }
    ]
  }
}
```
