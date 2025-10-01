import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: '',
        loadComponent: () => import('./views/vehicles-list/vehicles-list.component').then(m => m.VehiclesListComponent)
    },
    {
        path: 'vehiculos/nuevo',
        loadComponent: () => import('./views/create-vehicle/create-vehicle.component').then(m => m.CreateVehicleComponent)
    }
];
