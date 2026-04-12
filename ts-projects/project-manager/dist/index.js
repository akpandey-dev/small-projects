#!/usr/bin/env node
import * as fs from "fs";
const FILE = "data/projects.json";
let projects = [];
if (fs.existsSync(FILE)) {
    const data = fs.readFileSync(FILE, "utf-8");
    try {
        projects = JSON.parse(data);
    }
    catch {
        projects = [];
    }
}
function addProjects(title) {
    const newProject = {
        id: Date.now(),
        title,
        completed: false,
    };
    const project = projects.find((t) => t.title === title);
    if (!project) {
        projects.push(newProject);
        saveProjects();
        console.log("Project added: ", newProject);
    }
    else {
        console.log("[!]:Project with same title already added!");
        return;
    }
}
;
function deleteProjects(id) {
    let index = projects.findIndex(obj => obj.id === id);
    if (index !== -1) {
        projects.splice(index, 1);
    }
    ;
    saveProjects();
}
;
function listProjects() {
    if (projects.length === 0) {
        console.log("No projects yet!");
        return;
    }
    ;
    projects.forEach((project) => {
        console.log(`[${project.completed ? "✔" : "✕"}] ${project.id}: ${project.title}`);
    });
}
;
function completeProject(id) {
    const project = projects.find((t) => t.id === id);
    if (!project) {
        console.log("Project not found.");
        return;
    }
    project.completed = true;
    saveProjects();
    console.log("Project completed:", project.title);
}
function saveProjects() {
    fs.writeFileSync(FILE, JSON.stringify(projects, null, 2));
}
const args = process.argv.slice(2);
const command = args[0];
if (command === "add") {
    const title = args.slice(1).join(" ");
    addProjects(title);
}
else if (command === "list") {
    listProjects();
}
else if (command === "done") {
    const id = Number(args[1]);
    completeProject(id);
}
else if (command === "del" || command === "delete" || command === "remove") {
    const idArg = args[1];
    if (idArg === "all") {
        projects = [];
        saveProjects();
        console.log("All projects deleted.");
    }
    else {
        const id = Number(idArg);
        deleteProjects(id);
    }
}
else {
    console.log("Commands:");
    console.log(" add <project>");
    console.log(" list");
    console.log(" done <id>");
    console.log(" del <id>");
}
//# sourceMappingURL=index.js.map