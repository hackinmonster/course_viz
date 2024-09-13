import tkinter as tk

class Course:
    def __init__(self, name):
        self.name = name
        self.requisites = []

    def add_requisite(self, requisite):
        self.requisites.append(requisite)

class CourseVisualizer(tk.Canvas):
    def __init__(self, master, root_course, width=1000, height=800):
        super().__init__(master, width=width, height=height, bg="white")
        self.root_course = root_course
        self.node_radius = 20
        self.vertical_spacing = 100
        self.horizontal_padding = 40
        self.node_coords = {}
        
        self.v_scroll = tk.Scrollbar(master, orient="vertical", command=self.yview)
        self.h_scroll = tk.Scrollbar(master, orient="horizontal", command=self.xview)
        
        self.config(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)
        
        self.v_scroll.pack(side="right", fill="y")
        self.h_scroll.pack(side="bottom", fill="x")
        
        self.pack(side="left", fill="both", expand=True)

        self.calculate_positions(self.root_course, width // 2, 30)

        total_width = max(x for x, y in self.node_coords.values()) + self.node_radius + 50
        total_height = max(y for x, y in self.node_coords.values()) + self.node_radius + 50
        self.config(scrollregion=(0, 0, total_width, total_height))

        self.draw_tree(self.root_course)

    def calculate_positions(self, course, x, y):
        """ Recursively calculate positions of all nodes to avoid overlap. """
        if not course.requisites:
            self.node_coords[course] = (x, y)
            return self.node_radius * 2 

        total_width = 0
        child_positions = []
        num_children = len(course.requisites)
        child_x_start = x - (num_children * (self.node_radius + self.horizontal_padding)) // 2

        for child in course.requisites:
            subtree_width = self.calculate_positions(child, child_x_start, y + self.vertical_spacing)
            child_x_center = child_x_start + subtree_width / 2
            child_positions.append((child, child_x_center, y + self.vertical_spacing))
            child_x_start += subtree_width + self.horizontal_padding
            total_width += subtree_width + self.horizontal_padding

        total_width -= self.horizontal_padding
        self.node_coords[course] = (x, y)
        for child, child_x_center, child_y in child_positions:
            self.node_coords[child] = (child_x_center, child_y)
        
        return total_width

    def draw_tree(self, course):
        """ Recursively draw the tree starting from the given course. """
        x, y = self.node_coords[course]
        self.create_oval(x - self.node_radius, y - self.node_radius, 
                         x + self.node_radius, y + self.node_radius, 
                         fill="lightblue" if course.requisites else "lightgreen", outline="black")
        self.create_text(x, y, text=course.name, font=("Arial", 10, "bold"))

        for child in course.requisites:
            child_x, child_y = self.node_coords[child]
            self.create_line(x, y + self.node_radius, child_x, child_y - self.node_radius, arrow=tk.LAST, fill="black") 
            self.draw_tree(child)

root_course = Course("Root")


course1 = Course("Course 1")
course2 = Course("Course 2")
course3 = Course("Course 3")
course4 = Course("Course 4")
course5 = Course("Course 5")
course6 = Course("Course 6")
course7 = Course("Course 7")
course8 = Course("Course 8")
course9 = Course("Course 9")
course10 = Course("Course 10")
course11 = Course("Course 11")
course12 = Course("Course 12")
course13 = Course("Course 13")
course14 = Course("Course 14")
course15 = Course("Course 15")
course16 = Course("Course 16")
course17 = Course("Course 17")
course18 = Course("Course 18")
course19 = Course("Course 19")
course20 = Course("Course 20")
course21 = Course("Course 21")
course22 = Course("Course 22")
course23 = Course("Course 23")
course24 = Course("Course 24")
course25 = Course("Course 25")
course26 = Course("Course 26")
course27 = Course("Course 27")
course28 = Course("Course 28")
course29 = Course("Course 29")
course30 = Course("Course 30")

root_course.add_requisite(course1)

course3.add_requisite(course4)  
course1.add_requisite(course3)  
course1.add_requisite(course2)  
course2.add_requisite(course5)  
course3.add_requisite(course7)  
course3.add_requisite(course8)  
course8.add_requisite(course10)  
course8.add_requisite(course11)  
course5.add_requisite(course11)
course3.add_requisite(course12)  
course4.add_requisite(course13)  
course5.add_requisite(course14)  
course6.add_requisite(course15)  
course7.add_requisite(course16)  
course8.add_requisite(course17)  
course9.add_requisite(course18)  
course10.add_requisite(course19)  
course11.add_requisite(course20) 
course12.add_requisite(course21) 
course14.add_requisite(course23)  
course15.add_requisite(course24)  
course16.add_requisite(course25)  
course17.add_requisite(course26)  
course18.add_requisite(course27)  
course19.add_requisite(course28) 
course20.add_requisite(course29)  
course21.add_requisite(course30)  
course1.add_requisite(course16)  
course2.add_requisite(course18) 
course6.add_requisite(course9)  
course10.add_requisite(course23) 
course11.add_requisite(course24) 
course3.add_requisite(course25)  
course8.add_requisite(course26)  
course5.add_requisite(course30)  


root_window = tk.Tk()
root_window.title("Course Tree Visualization with Scrollbars")
course_visualizer = CourseVisualizer(root_window, root_course)
root_window.mainloop()
