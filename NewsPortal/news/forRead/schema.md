```yaml
openapi: 3.0.2
info:
  title: 'Портал новостей OpenApi спецификация'
  version: "0.1"
servers:
  - url: http://127.0.0.1:8004/
    description: ''
paths:
  /api/posts/:
    get:
      operationId: listPost
      description: 'List of posts'
      responses:
        '200':
          content:
          application/json:
            schema:
              type: object
              properties:
                count:
                  type: integer
                  example: 123
                next:
                  type: string
                  nullable: true
                  format: uri
                  example: http://api.example.org/accounts/?offset=400&limit=100
                previous:
                  type: string
                  nullable: true
                  format: uri
                  example: http://api.example.org/accounts/?offset=200&limit=100
                results:
                  type: array
                  items:
                    $ref: '#/components/schemas/Post'
      tags:
        - posts
    post:
      operationId: createPost
      description: 'create Post'
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Post'
          application/x-www-form-urlencoded:
            schema:
               $ref: '#/components/schemas/Post'
          multipart/form-data:
            schema:
               $ref: '#/components/schemas/Post'
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Post'
          description: ''
      tags:
        - posts
  /api/posts/{id}:
    get:
      operationId: detailPost
      description: ''
      parameters:
      - name: id


components:
  schemas:
    Post:
      type: object
      properties:
        id:
          type: integer
          readOnly: true
        title:
          type: string
          maxLength: 64
        content:
          type: string
          maxLength: 20
        rate_new:
          type: integer
      required:
          - title
```

"user": {
    "id": 1,
    "username": "rasen",
    "first_name": "rasen",
    "last_name":
}


openapi: 3.0.2
info:
  title: 'Портал новостей OpenApi спецификация'
  version: "0.1"
servers:
  - url: http://127.0.0.1:8004/
    description: ''
paths:
  /api/authors/:
    get:
      summary: Метод получения авторов
      operationId: listAuthors
      responses:
        '200':
          description: Ответ со списком авторов
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Author'
        'default':
          description: Нестандартный ответ
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Author'
      tags:
      - authors
    post:
      summary: Метод создания автора
      operationId: createAuthor
      description: 'create Author'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Author'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Author'
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/Author'
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Author'
          description: ''
      tags:
      - authors
  /api/authors/{id}/:
    get:
      operationId: getAuthorId
      description: ''
      parameters:
      - name: id
        in: path
        required: true
        description: A unique integer value identifying this author.
        schema:
          type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Author'
          description: ''
      tags:
      - authors

components:
  schemas:
    Author:
      type: object
      required: true
      properties:
        user:
          type: string
          description: 'Пользователь'
    Authors:
      type: array
      items:
        $ref: '#/components/schemas/Author'
    Error:
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: integer
        message:
          type: string