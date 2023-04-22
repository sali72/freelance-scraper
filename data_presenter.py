import pandas as pd
# import matplotlib.pyplot as plt

class DataPresenter:
    def draw_line_chart(self, projects, fig):
        df = self.scalars_to_df(projects)
        
    
        # list of squares
        return  [i**2 for i in range(101)]
    
        
        
    def scalars_to_df(self, scalars_projects):
        list_projects = []
        for p_obj in scalars_projects:
            project = []
            project.append(p_obj.id)
            project.append(p_obj.title)
            project.append(p_obj.url)
            project.append(p_obj.description)
            project.append(p_obj.posted_date)
            project.append(p_obj.deadline)
            project.append(p_obj.expected_time_limit)
            project.append(p_obj.price_fixed)
            project.append(p_obj.price_fixed_min)
            project.append(p_obj.price_hourly)
            project.append(p_obj.price_hourly_min)
            # TODO tags

            list_projects.append(project)
        return pd.DataFrame(list_projects ,columns=["index","title","url","description","posted_date","deadline","expected_time_limit",\
                                "price_fixed","price_fixed_min","price_hourly","price_hourly_min"])
