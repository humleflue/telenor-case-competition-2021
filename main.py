import pandas
import pm4py
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

def import_csv(file_path):
    log = pandas.read_csv(file_path, sep=';')

    num_events = len(log)
    num_cases = len(log.key.unique())
    print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))

    log = pm4py.format_dataframe(log, case_id='key', activity_key='action', timestamp_key='timestamp')

    start_activities = pm4py.get_start_activities(log)
    end_activities = pm4py.get_end_activities(log)
    print("Start activities: {}\nEnd activities: {}".format(start_activities, end_activities))

    process_tree = pm4py.discover_process_tree_inductive(log)
    bpmn_model = pm4py.convert_to_bpmn(process_tree)
    pm4py.save_vis_bpmn(bpmn_model, "./Images/bpmn_model.png")

    dfg, start_activities, end_activities = pm4py.discover_dfg(log)
    pm4py.save_vis_performance_dfg(dfg, start_activities, end_activities, "./Images/dfg.png")

    map = pm4py.discover_heuristics_net(log)
    pm4py.save_vis_heuristics_net(map, "./Images/heuristics_net.png")

if __name__ == "__main__":
    import_csv("./process_dump.csv")
