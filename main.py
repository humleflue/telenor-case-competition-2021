import pandas
import pm4py
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

def import_csv(file_path):
    event_log = pandas.read_csv(file_path, sep=';')
    event_log = pm4py.format_dataframe(event_log, case_id='key', activity_key='action', timestamp_key='timestamp')
    # start_activities = pm4py.get_start_activities(event_log)
    # end_activities = pm4py.get_end_activities(event_log)
    # print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))
    process_tree = pm4py.discover_process_tree_inductive(event_log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.view_bpmn(bpmn_model)

if __name__ == "__main__":
    import_csv("./process_dump.csv")
