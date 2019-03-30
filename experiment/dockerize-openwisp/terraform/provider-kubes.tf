provider "kubernetes" {
  host = "http://127.0.0.1:8081"
}

resource "kubernetes_replication_controller" "openwisp" {
  metadata {
    name = "openwisp"

    labels {
      App = "openwisp"
    }
  }

  spec {
    replicas = 3

    selector {
      App = "openwisp"
    }

    template {
      metadata {
        labels {
          App = "openwisp"
        }
      }

      spec {
        container {
          image   = "atb00ker/ready-to-run:private-network-topology"
          name    = "openwisp-private-network-topology"

          port {
            container_port = 8001
          }

        }
        container {
          image   = "atb00ker/ready-to-run:private-controller"
          name    = "openwisp-private-controller"

          port {
            container_port = 8000
          }

          env {
            name  = "DJANGO_REDIS_HOST"
            value = "localhost"
          }
        }

        container {
          image = "redis:alpine"
          name  = "redis"
        }
      }
    }
  }
}

resource "kubernetes_service" "openwisp" {
  metadata {
    name = "openwisp"
  }

  spec {
    selector {
      App = "${kubernetes_replication_controller.openwisp.metadata.0.labels.App}"
    }

    port {
      port        = 8000
      target_port = 8000
    }
    port {
      port        = 8001
      target_port = 8001
    }

    external_ips = ["192.168.1.6"]
    type         = "LoadBalancer"
  }
}
