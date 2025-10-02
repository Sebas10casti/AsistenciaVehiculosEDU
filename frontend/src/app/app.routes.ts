import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: '',
        redirectTo: 'vehiculos',
        pathMatch: 'full'
    },
    {
        path: 'vehiculos',
        loadComponent: () => import('./views/vehicles-list/vehicles-list.component').then(m => m.VehiclesListComponent)
    },
    {
        path: 'vehiculos/nuevo',
        loadComponent: () => import('./views/create-vehicle/create-vehicle.component').then(m => m.CreateVehicleComponent)
    },
    {
        path: 'registros',
        loadComponent: () => import('./views/register-list/register-list.component').then(m => m.RegisterListComponent)
    },
    {
        path: 'registros/nuevo',
        loadComponent: () => import('./views/register-start/register-start.component').then(m => m.RegisterStartComponent)
    },
    {
        path: 'registros/finalizar',
        loadComponent: () => import('./views/register-end/register-end.component').then(m => m.RegisterEndComponent)
    }
];
