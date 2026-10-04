from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Defining the model structure (edges)
model = BayesianNetwork([('CPU', 'Overload'), ('Memory', 'Overload')])

# Defining the Conditional Probability Distributions (CPDs)

# CPU usage distribution (probability for 2 states: Low and High)
cpu_cpd = TabularCPD(variable='CPU', variable_card=2, values=[[0.7], [0.3]])  # 0 for Low, 1 for High

# Memory usage distribution (probability for 2 states: Low and High)
memory_cpd = TabularCPD(variable='Memory', variable_card=2, values=[[0.8], [0.2]])  # 0 for Low, 1 for High

# Defining the Conditional Probability Distribution (CPD) for Overload given CPU and Memory
overload_cpd = TabularCPD(variable='Overload', variable_card=2,
                          values=[[0.95, 0.2, 0.6, 0.9],  # P(Overload=Low | CPU, Memory)
                                  [0.05, 0.8, 0.4, 0.1]],  # P(Overload=High | CPU, Memory)
                          evidence=['CPU', 'Memory'],
                          evidence_card=[2, 2])

# Adding the CPDs to the model
model.add_cpds(cpu_cpd, memory_cpd, overload_cpd)

# Checking if the model is valid
print("Model is valid:", model.check_model())

# Performing inference
inference = VariableElimination(model)

# Query the model: what is the probability of Overload given that CPU is High and Memory is Low?
result = inference.query(variables=['Overload'], evidence={'CPU': 1, 'Memory': 0})  # 1 for High, 0 for Low
print(result)