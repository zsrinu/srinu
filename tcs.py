
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a structure for Animal
struct Animal {
    char *name;
    int age;
    void (*makeSound)(void);
    void (*displayInfo)(struct Animal*);
};

// Define functions to simulate methods
void makeAnimalSound() {
    printf("The animal makes a sound\n");
}

void displayAnimalInfo(struct Animal *animal) {
    printf("Name: %s\n", animal->name);
    printf("Age: %d\n", animal->age);
}

// Constructor for Animal
struct Animal* createAnimal(char *name, int age) {
    struct Animal *animal = (struct Animal*)malloc(sizeof(struct Animal));
    animal->name = strdup(name);
    animal->age = age;
    animal->makeSound = makeAnimalSound;
    animal->displayInfo = displayAnimalInfo;
    return animal;
}

// Define a structure for Dog, inheriting Animal
struct Dog {
    struct Animal base;
};

// Constructor for Dog
struct Dog* createDog(char *name, int age) {
    struct Dog *dog = (struct

