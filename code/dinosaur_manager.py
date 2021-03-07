from veterinarian import *
from lab import *

def euthanize_dinosaurs():
    for dinosaur in get_dinosaurs():
        print(f"Euthanizing {dinosaur}")

def run_experiments():
    for dinosaur in get_dinosaurs():
        print(f"Running experiment on {dinosaur}")
