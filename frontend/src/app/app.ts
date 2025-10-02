import { Component, signal } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" routerLink="/">Parqueadero</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link" routerLink="/" routerLinkActive="active">Vehículos</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" routerLink="/vehiculos/nuevo" routerLinkActive="active">Registrar Vehículo</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" routerLink="/registros" routerLinkActive="active">Registros</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" routerLink="/registros/nuevo" routerLinkActive="active">Registrar Ingreso</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" routerLink="/registros/finalizar" routerLinkActive="active">Registrar Salida</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-outlet></router-outlet>
  `,
})
export class App {
  protected readonly title = signal('frontend');
}
