import unittest
import subprocess
import urllib.request 
import json
import math
import random
import numpy as np 
import time

class Test(unittest.TestCase):

    child_process = None

    def setUp(self):
        self.child_process = subprocess.Popen(args=['python', 'mathapi.py'], stdout=None)
        time.sleep(2) # Give server time to come up

    def tearDown(self):
        try: 
            self.child.terminate()
            self.child.kill()
        except:
            print('Error terminating server child process')

    def test_square_area(self):
        for side in [1,4,7,8,99]:
            req = urllib.request.Request('http://localhost:3001/area/square?s=' + str(side))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on square area request')
            
            self.assertEqual(200, response.getcode(), 'Square area did not return 200 status code');
            self.assertEqual({'s': side, 'a': (side * side)}, data, 'Square area JSON incorrect')

    def test_rectangle_area(self):
        for dimensions in [(1,1), (2,5), (8, 2), (200, 300)]:
            req = urllib.request.Request('http://localhost:3001/area/rectangle?l=' + str(dimensions[0]) + '&w=' + str(dimensions[1]))
            response = urllib.request.urlopen(req)
            try: 
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on rectangle area request')
            self.assertEqual(200, response.getcode(), 'Rectangle area did not return 200 status code');
            self.assertEqual({'l': dimensions[0], 'w': dimensions[1], 'a': dimensions[1] * dimensions[0]}, data, 'Rectangle area JSON incorrect')

    def test_triangle_area(self):
        for dimensions in [(1,1), (2,5), (8, 2), (200, 300)]:
            req = urllib.request.Request('http://localhost:3001/area/triangle?b=' + str(dimensions[0]) + '&h=' + str(dimensions[1]))
            response = urllib.request.urlopen(req)
            try: 
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on triangle area request')
            self.assertEqual(200, response.getcode(), 'Triangle area did not return 200 status code');
            self.assertEqual({'b': dimensions[0], 'h': dimensions[1], 'a': dimensions[1] * dimensions[0] / 2}, data, 'Triangle area JSON incorrect')

    def test_heron(self):
        for dimensions in [(1,2,3), (3,6,9), (100, 200, 150)]:
            req = urllib.request.Request('http://localhost:3001/area/heron?x=' + str(dimensions[0]) + '&y=' + str(dimensions[1]) + '&z=' + str(dimensions[2]))
            response = urllib.request.urlopen(req)
            try: 
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on heron area request')

            x = dimensions[0]
            y = dimensions[1]
            z = dimensions[2]
            s = (x + y + z) / 2
            a = math.sqrt((s * (s - x) * (s - y) * (s - z)))

            self.assertEqual(200, response.getcode(), 'Heron area did not return 200 status code')
            self.assertEqual({'x': x, 'y': y, 'z': z, 's': s, 'a': a}, data, 'Heron area JSON incorrect')

    def test_parallelogram(self):
        for x in range(10):
            b = random.randint(2, 100)
            h = random.randint(2, 100)
            req = urllib.request.Request('http://localhost:3001/area/parallelogram?b=' + str(b) + '&h=' + str(h))
            response = urllib.request.urlopen(req)
            try: 
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on parallelogram test')
            self.assertEqual(200, response.getcode(), 'Parallelogram did not return 200 status code')
            self.assertEqual({'b': b, 'h': h, 'a': (b * h)}, data, 'JSON incorrect for parallelogram')

    def test_circle(self):
        for x in range(10):
            r = random.randint(2, 100)
            req = urllib.request.Request('http://localhost:3001/area/circle?r=' + str(r))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on circle area test')
            self.assertEqual(200, response.getcode(), 'Circle area did not return 200 status code')
            self.assertEqual(self.round_dictionary({'r': r, 'a': (math.pi * r * r)}), self.round_dictionary(data), 'JSON incorrect for circle area')
            
    def test_trapezoid_area(self):
        for x in range(10):
            h = random.randint(2, 100)
            b1 = random.randint(2, 100)
            b2 = random.randint(2, 100)
            a = ((b1 + b2) / 2) * h
            req = urllib.request.Request('http://localhost:3001/area/trapezoid?h=' + str(h) + '&b1=' + str(b1) + '&b2=' + str(b2))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on trapezoid area test')
            self.assertEqual(200, response.getcode(), 'Trapezoid area did not return 200 status code')
            self.assertEqual(self.round_dictionary({'h': h, 'b1': b1, 'b2': b2, 'a': a}), self.round_dictionary(data)); 

    #####################
    ## Surface Area Tests
    def test_cube_surface_area(self):
        for x in range(10):
            s = random.randint(2, 100)
            a = 6 * s * s
            req = urllib.request.Request('http://localhost:3001/surface/cube?s=' + str(s))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on cube surface area test')
            self.assertEqual(200, response.getcode(), 'Cube surface area did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'s': s, 'sa': a}), self.round_dictionary(data))

    def test_sphere_surface_area(self):
        for x in range(10):
            r = random.randint(2, 100)
            a = 4 * math.pi * r * r
            req = urllib.request.Request('http://localhost:3001/surface/sphere?r=' + str(r))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on sphere surface area test')
            self.assertEqual(200, response.getcode(), 'Sphere surface area did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'r': r, 'sa': a}), self.round_dictionary(data))

    def test_cylinder_surface_area(self):
        for x in range(10):
            r = random.randint(2, 100)
            h = random.randint(2, 100)
            a = (2 * math.pi * r * h) + (2 * math.pi * r * r)
            req = urllib.request.Request('http://localhost:3001/surface/cylinder?r=' + str(r) + '&h=' + str(h))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on cylinder surface area test')
            self.assertEqual(200, response.getcode(), 'Cylinder surface area did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'r': r, 'h': h, 'sa': a}), self.round_dictionary(data))


    #############
    ## Perimeters
    def test_square_perimeter(self):
        for x in range(10):
            s = random.randint(2, 100)
            p = 4 * s
            req = urllib.request.Request('http://localhost:3001/perimeter/square?s=' + str(s))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on square perimeter test')
            self.assertEqual(200, response.getcode(), 'Square perimeter did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'s': s, 'p': p}), self.round_dictionary(data))

    def test_rectangle_perimeter(self):
        for x in range(10):
            l = random.randint(2, 100)
            w = random.randint(2, 100)
            p = (2 * l) + (2 * w)
            req = urllib.request.Request('http://localhost:3001/perimeter/rectangle?l=' + str(l) + '&w=' + str(w))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on rectangle perimeter test')
            self.assertEqual(200, response.getcode(), 'Rectangle perimeter did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'l': l, 'w': w, 'p': p}), self.round_dictionary(data))

    def test_triangle_perimeter(self):
        for x in range(10):
            s1 = random.randint(2, 100)
            s2 = random.randint(2, 100)
            s3 = random.randint(2, 100)
            p = s1 + s2 + s3
            req = urllib.request.Request('http://localhost:3001/perimeter/triangle?s1=' + str(s1) + '&s2=' + str(s2) + '&s3=' + str(s3))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on triangle perimeter test')
            self.assertEqual(200, response.getcode(), 'Triangle perimeter did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'s1': s1, 's2': s2, 's3': s3, 'p': p}), self.round_dictionary(data))

    def test_circle_circumference(self):
        for x in range(10):
            d = random.randint(2, 100)
            c = d * math.pi
            req = urllib.request.Request('http://localhost:3001/perimeter/circle?d=' + str(d))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on circle perimeter test')
            self.assertEqual(200, response.getcode(), 'Circle perimeter did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'d': d, 'c': c}), self.round_dictionary(data))

    ################
    ## Volume Routes
    def test_cube_volume(self):
        for x in range(10):
            s = random.randint(2, 100)
            v = s * s * s
            req = urllib.request.Request('http://localhost:3001/volume/cube?s=' + str(s))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on cube volume test')
            self.assertEqual(200, response.getcode(), 'Cube volume did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'s': s, 'v': v}), self.round_dictionary(data))

    def test_prism_volume(self):
        for x in range(10):
            l = random.randint(2, 100)
            w = random.randint(2, 100)
            h = random.randint(2, 100)
            v = l * w * h
            req = urllib.request.Request('http://localhost:3001/volume/prism?l=' + str(l) + '&h=' + str(h) + '&w=' + str(w))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on prism volume test')
            self.assertEqual(200, response.getcode(), 'Prism volume did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'l': l, 'w': w, 'h': h, 'v': v}), self.round_dictionary(data))

    def test_pyramid_volume(self):
        for x in range(10):
            b = random.randint(2, 100)
            h = random.randint(2, 100)
            v = (b * b * h) / 3
            req = urllib.request.Request('http://localhost:3001/volume/pyramid?b=' + str(b) + '&h=' + str(h))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on pyramid volume test')
            self.assertEqual(200, response.getcode(), 'Pyramid volume did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'b': b, 'h': h, 'v': v}), self.round_dictionary(data))
    def test_cylinder_volume(self):
        for x in range(10):
            r = random.randint(2, 100)
            h = random.randint(2, 100)
            v = math.pi * r * r * h
            req = urllib.request.Request('http://localhost:3001/volume/cylinder?r=' + str(r) + '&h=' + str(h))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on cylinder volume test')
            self.assertEqual(200, response.getcode(), 'Cylinder volume did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'r': r, 'h': h, 'v': v}), self.round_dictionary(data))

    def test_sphere_volume(self):
        for x in range(10):
            r = random.randint(2, 100)
            v = (4 * math.pi * r * r * r / 3)
            req = urllib.request.Request('http://localhost:3001/volume/sphere?r=' + str(r))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on sphere volume test')
            self.assertEqual(200, response.getcode(), 'Sphere volume did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'r': r, 'v': v}), self.round_dictionary(data))

    def test_cone_volume(self):
        for x in range(10):
            r = random.randint(2, 100)
            h = random.randint(2, 100)
            v = (math.pi * r * r * h) / 3
            req = urllib.request.Request('http://localhost:3001/volume/cone?r=' + str(r) + '&h=' + str(h))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on cone volume test')
            self.assertEqual(200, response.getcode(), 'Cone volume did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'r': r, 'h': h, 'v': v}), self.round_dictionary(data))

    #############
    ## Misc Tests
    def test_distance_formula(self):
        for x in range(10):
            x1 = random.randint(-100, 100)
            y1 = random.randint(-100, 100)
            x2 = random.randint(-100, 100)
            y2 = random.randint(-100, 100)
            d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
            req = urllib.request.Request('http://localhost:3001/distance?x1=' + str(x1) + '&y1=' + str(y1) + '&x2=' + str(x2) + '&y2=' + str(y2))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on distance formula test')
            self.assertEqual(200, response.getcode(), 'Distance formula did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'d': d, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2}), self.round_dictionary(data))

    def test_slope(self):
        for x in range(10):
            x1 = random.randint(-100, 100)
            y1 = random.randint(-100, 100)
            x2 = random.randint(-100, 100)
            y2 = random.randint(-100, 100)
            m = (y2 - y1) / (x2 - x1)
            req = urllib.request.Request('http://localhost:3001/slope?x1=' + str(x1) + '&y1=' + str(y1) + '&x2=' + str(x2) + '&y2=' + str(y2))
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on slope test')
            self.assertEqual(200, response.getcode(), 'Slope test did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'m': m, 'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2}), self.round_dictionary(data))

    def test_pythagorean(self):
        for triplet in [(3,4,5), (5, 12, 13), (9, 40, 41), (11, 60, 61), (12, 35, 37),(13, 84, 85)]:
            a = triplet[0]
            b = triplet[1]
            c = triplet[2]

            test = random.randint(1,3)
            
            if test == 1:
                # A, B; solve for C
                qs = '?a=' + str(a) + '&b=' + str(b)
            elif test == 2:
                # B, C; solve for A
                qs = '?b=' + str(b) + '&c=' + str(c)
            else:
                # A, C; solve for B
                qs = '?a=' + str(a) + '&c=' + str(c); 

            req = urllib.request.Request('http://localhost:3001/pythag' + qs)
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on pythagorean test')
            self.assertEqual(200, response.getcode(), 'Pythagorean test did not return a 200 status code')
            self.assertEqual(self.round_dictionary({'a': a, 'b': b, 'c': c}), self.round_dictionary(data))

    def test_average(self):
        for x in range(10):
            ray = np.random.randint(1, 100, random.randint(3, 20)).tolist()
            str_ray = ','.join([str(int) for int in ray])
            avg = np.average(ray)
            req = urllib.request.Request('http://localhost:3001/average?nums=' + str_ray)
            response = urllib.request.urlopen(req)
            try:
                data = json.loads(response.read())
            except:
                self.fail('Could not parse JSON on average test')
            self.assertEqual(200, response.getcode(), 'Average test did not return a 200 status code')
            self.assertTrue('avg' in data, 'avg element not found in JSON for average route')
            self.assertAlmostEqual(avg, data['avg'], 5)


    ##########
    ## Helpers
    def round_dictionary(self, dict, places=3):
        return {key: round(dict[key], places) for key in dict}

if __name__ == '__main__':
    unittest.main()
