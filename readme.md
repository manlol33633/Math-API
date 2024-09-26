[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/IZofgfIn)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12522352)
## Math API Server

This time we're going to write an API server that solves math problems for us. Each route is a different formula to solve, and values will be passed as GET arguments.

Let's look at the area of a square route below. The route is listed as `/area/square` with one variable `s`. Calling `http://localhost:3001/area/square?s=10` should return JSON with the answer.  For that route the JSON returned would be.

```json
{
    "a": 100,
    "s": 10
}
```

_Note that they keys in the JSON are lower case._

Each route must return any variables passed and the solution. Use the letters in the formulas listed as keys.

Routes must also return their data with the `application/json` content type and a `200` status code header, assuming it was a good request. 

There are two "bad requests" that you also need to account for.

* Incorrect route. This needs to return a 404 status header. 
* Invalid or missing GET variables. This should return a 400 status header. This would be cases like `/area/square?x=10` where the variable is `x` instead of `s` or just calling `/area/square` without any variables. 



Your code needs to start in the `mathapi.py` file, but you can add additional files if you would like. Running `python mathapi.py` should start your server.

The server needs to be attached to `127.0.0.1` on port `3001`

### Area Routes

#### Square

`/area/square`

![area-square](img/readme/area-square.png)



| Variable | Description |
| -------- | ----------- |
| s        | Side length |



#### Rectangle

`/area/rectangle` 

![area-rectangle](img/readme/area-rectangle.png)



| Variable           | Description         |
| ------------------ | ------------------- |
| l (lower case ell) | Length of rectangle |
| w                  | Width of rectangle  |



#### Triangle

`/area/triangle`

![area-triangle](img/readme/area-triangle.png)



| Variable | Description        |
| -------- | ------------------ |
| b        | Base of Triangle   |
| h        | Height of triangle |



#### Triangle - Heron's Formula

`/area/heron`

![heron](img/readme/heron.png)



| Variable | Description   |
| -------- | ------------- |
| x        | Side length x |
| y        | Side length y |
| z        | Side length z |

On this one, `s` should also be included in the returned JSON.



#### Parallelogram

`/area/parallelogram`

![area-parallelogram](img/readme/area-parallelogram.png)

| Variables | Description    |
| --------- | -------------- |
| b         | Base dimension |
| h | Height of parallelogram |





#### Circle

`/area/circle`

![area-circle](img/readme/area-circle.png)

Use `math.pi` instead of 3.14

| Variable | Notes                |
| -------- | -------------------- |
| r        | Radius of the circle |





#### Trapezoid

`/area/trapezoid`

![area-trapezoid](img/readme/area-trapezoid.png)



| Variables | Notes                   |
| --------- | ----------------------- |
| b1        | Length of one base      |
| b2        | Length of other base    |
| h         | Height of the trapezoid |



### Surface Area Routes

#### Cube

`/surface/cube`

![surface-cube](img/readme/surface-cube.png)

| Variable | Notes                   |
| -------- | ----------------------- |
| s        | Side length of the cube |



#### Sphere

`/surface/sphere`

![surface-sphere](img/readme/surface-sphere.png)

Use `math.pi` instead of 3.14

| Variable | Notes            |
| -------- | ---------------- |
| r        | Radius of sphere |



#### Cylinder

`/surface/cylinder`

![surface-cylinder](img/readme/surface-cylinder.png)

| Variables | Notes                  |
| --------- | ---------------------- |
| r         | Radius of the cylinder |
| h         | Height of the cylinder |





### Perimeter Routes 

#### Square

`/perimeter/square`

![perimeter-square](img/readme/perimeter-square.png)

| Variable | Notes                     |
| -------- | ------------------------- |
| s        | Side length of the square |





#### Rectangle

`/perimeter/rectangle`

![perimeter-rectangle](img/readme/perimeter-rectangle.png)

| Variables          | Notes                   |
| ------------------ | ----------------------- |
| l (lower case ell) | Length of the rectangle |
| w                  | Width of the rectangle  |



#### Triangle

`/perimeter/triangle`

![perimeter-triangle](img/readme/perimeter-triangle.png)

| Variable | Notes                   |
| -------- | ----------------------- |
| s1       | Side length of triangle |
| s2       | Side length of triangle |
| s3       | Side length of triangle |



#### Circle (Circumference)

`/perimeter/circle`

![perimeter-circle](img/readme/perimeter-circle.png)

| Variable | Notes           |
| -------- | --------------- |
| d        | Circle diameter |



### Volume Routes

#### Cube

`/volume/cube`

![vol-cube](img/readme/vol-cube.png)

| Variable | Notes       |
| -------- | ----------- |
| s        | side length |



#### Rectangular Prism

`/volume/prism`

![vol-rect](img/readme/vol-rect.png)

| Variable | Notes  |
| -------- | ------ |
| l        | Length |
| w        | Width  |
| h        | Height |



#### Square Pyramid

`/volume/pyramid`

![vol-squarepyramid](img/readme/vol-squarepyramid.png)

| Variable | Notes  |
| -------- | ------ |
| b        | Base   |
| h        | Height |





#### Cylinder

`/volume/cylinder`

![vol-cylinder](img/readme/vol-cylinder.png)

| Variable | Notes              |
| -------- | ------------------ |
| r        | Radius of circle   |
| h        | Height of cylinder |



#### Cone

`/volume/cone`

![vol-cone](img/readme/vol-cone.png)

| Variable | Notes              |
| -------- | ------------------ |
| r        | Radius of circle   |
| h        | Height of cylinder |

#### Sphere

`/volume/sphere`

![vol-sphere](img/readme/vol-sphere.png)

| Variable | Notes            |
| -------- | ---------------- |
| r        | Radius of sphere |



### Misc Routes

#### Distance Formula

`/distance`

![distance](img/readme/distance.png)

| Variable | Notes                    |
| -------- | ------------------------ |
| x1, y1   | Position of first point  |
| x2, y2   | Position of second point |





#### Slope

`/slope`

![lineslope](img/readme/lineslope.png)

| Variable | Notes                    |
| -------- | ------------------------ |
| x1, y1   | Position of first point  |
| x2, y2   | Position of second point |

#### Pythagorean Theorem

`/pythag`

![pythag](img/readme/pythag.png)

Use to solve for the third side in a right triangle. 

This one is going to be a little different than most of the other routes. You'll only send 2 of the 3 variables and your implementation should solve for the third. 

The JSON returned will contain all 3 values.

Calls to `/pythag?a=3&b=4`, `/pythag?b=4&c=5` & `/pythag?a=3&c=5` should all return the same JSON below. 

```json
{
    "a": 3,
    "b": 4,
    "c": 5
}
```





#### Average

`/average`

![mean](img/readme/mean.png)

Solve for the average of all numbers passed as a comma separated list. 

| Variable | Description                                                  |
| -------- | ------------------------------------------------------------ |
| nums     | A comma separated list of integers to average. For example, if you want to average the numbers 1, 2, & 3 the route would look like `/average?nums=1,2,3` |

In the JSON returned, the values should be returned as an array. For example, `/mean?nums=1,2,3` should return the following JSON.

```json
{
    "avg": 2,
    "nums": [
        1,
        2,
        3
    ]
}
```



