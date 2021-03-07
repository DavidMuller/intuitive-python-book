from veterinarian import get_dinosaurs as get_dinosaurs_at_vet
from lab import get_dinosaurs as get_dinosaurs_at_lab

def euthanize_dinosaurs():
    for dinosaur in get_dinosaurs_at_vet():
        print(f"Euthanizing {dinosaur}")

def run_experiments():
    for dinosaur in get_dinosaurs_at_lab():
        print(f"Running experiment on {dinosaur}")
