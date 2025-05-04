advices = [
    "Повторение — мать учения.",
    "Ученье — свет, а неученье — тьма.",
    "Знания – сила.",
    "Грамоте учиться – всегда пригодится.",
    "Не стыдно не знать – стыдно не учиться.",
    "Без муки нет науки."
]

document.querySelector("#advice-text").textContent = advices[Math.floor(Math.random()*advices.length)];