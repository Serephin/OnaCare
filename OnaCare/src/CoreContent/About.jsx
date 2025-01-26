import React from 'react'
import Zerda from "../../public/zerda.webp"

function About() {
    return (

        <div class="flex max-w-6xl ">
            <div class="flex-none w-48 relative">
                <img src={Zerda} alt="" class="absolute inset-0 w-full h-full object-cover" loading="lazy" />
            </div>
            <form class="flex-auto p-6">
                <div class="flex flex-wrap">
                    <h1 class="flex-auto text-lg font-semibold text-slate-900">
                        Марина Тилляева
                    </h1>

                    <div class="w-full flex-none text-sm font-medium text-slate-700 mt-2">
                    +998944094093
                    </div>
                    <div class="w-full flex-none text-sm font-medium text-slate-700 mt-2">
                    ул.Мукими Блок-Е
                    </div>
                    <div class="w-full flex-none text-sm font-medium text-slate-700 mt-2">
                    неделя беремености 18 
                    </div>
                </div>
                <div class="flex items-baseline mt-4 mb-6 pb-6 border-b border-slate-200">

                </div>
                <div class="flex space-x-4 mb-6 text-sm font-medium">

                </div>

            </form>
        </div>
    )
}

export default About